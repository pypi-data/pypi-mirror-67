from celery import Task
from celery.states import FAILURE
from socketio import RedisManager


class StirfriedTask(Task):
    _sio = None

    @property
    def have_redis(self):
        return bool(self.app.conf.get("stirfried_redis_url"))

    @property
    def sio(self):
        """Property that ensures each Task instance (1 per worker process) uses
        a single Redis connection for Socket.IO communication for all of its
        task invocations.

        Note that the user must configure `app.conf.stirfried_redis_url` via standard
        Celery config mechanisms.
        """
        if self._sio is None and self.have_redis:
            self._sio = RedisManager(self.app.conf.stirfried_redis_url, write_only=True)
        return self._sio

    @property
    def error_info(self):
        return bool(self.app.conf.get("stirfried_error_info", False))

    @property
    def sentinel_room(self):
        return self.app.conf.get("stirfried_sentinel_room", "NO_EMIT")

    def emit_progress(self, current, total, info=None):
        """Emits task invocation progress.

        Note that this callback must be called by the user in the task body.
        """
        if not self.have_redis or self.request.kwargs["room"] == self.sentinel_room:
            return
        self.sio.emit(
            "on_progress",
            room=self.request.kwargs["room"],
            data=dict(
                # callback arguments
                current=current,
                total=total,
                info=info,
                # additional info
                task_id=self.request.id,
                task_name=self.name,
            ),
        )

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        """Emits when task invocation fails and is retried.

        Note that this callback is called automatically by Celery.
        """
        if self.have_redis and kwargs["room"] != self.sentinel_room:
            data = dict(task_id=task_id, task_name=self.name)
            if self.error_info:
                data["einfo"] = str(einfo)
            self.sio.emit("on_retry", room=kwargs["room"], data=data)
        super().on_retry(exc, task_id, args, kwargs, einfo)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """Emits when task invocation fails.

        Note that this callback is called automatically by Celery.
        """
        if self.have_redis and kwargs["room"] != self.sentinel_room:
            data = dict(task_id=task_id, task_name=self.name)
            if self.error_info:
                data["einfo"] = str(einfo)
            self.sio.emit("on_failure", room=kwargs["room"], data=data)
        super().on_failure(exc, task_id, args, kwargs, einfo)

    def on_success(self, retval, task_id, args, kwargs):
        """Emits when task invocation succeeds.

        Note that this callback is called automatically by Celery.
        """
        if self.have_redis and kwargs["room"] != self.sentinel_room:
            data = dict(retval=retval, task_id=task_id, task_name=self.name)
            self.sio.emit("on_success", room=kwargs["room"], data=data)
        super().on_success(retval, task_id, args, kwargs)

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        """Emits when task invocation returns (success/failure).

        Note that this callback is called automatically by Celery.
        """
        if self.have_redis and kwargs["room"] != self.sentinel_room:
            retval_ = retval
            if status == FAILURE:
                retval_ = str(retval_) if self.error_info else None
            data = dict(
                status=status, retval=retval_, task_id=task_id, task_name=self.name
            )
            self.sio.emit("on_return", room=kwargs["room"], data=data)
        super().after_return(status, retval, task_id, args, kwargs, einfo)
