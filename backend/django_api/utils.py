import datetime
import time
from rest_framework.request import Request
from rest_framework.response import Response
from django_app import models


def logging_decorator(func_controller: callable) -> any:
    def __wrapper(request: Request, *args, **kwargs) -> Response:
        time_start_func = time.perf_counter()
        # print(_request.META.get("REMOTE_ADDR"), _request.META.get("COMPUTERNAME"), _request.META.get("USERNAME"))

        result = func_controller(request, *args, **kwargs)
        time_stop_func = time.perf_counter()
        time_elapsed = round(time_stop_func - time_start_func, 5)

        models.LoggingModel.objects.create(
            user=request.user if request.user.username else None,
            ip=request.META.get("REMOTE_ADDR"),
            path=request.path,
            method=request.method,
            text=f"[{time_elapsed}]",
        )
        text = f"\ntime: {datetime.datetime.now()} user: {request.user if request.user.username else None} ip: " \
               f"{request.META.get('REMOTE_ADDR')} path: {request.path} method: {request.method} action: " \
               f"_request.action response: [{time_elapsed}]"
        with open('static/media/logging_actions.txt', 'a') as log:
            log.write(text)

        return result
    return __wrapper
