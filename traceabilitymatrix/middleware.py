from django.http import JsonResponse
import datetime


class CustomExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        exception_type = type(exception).__name__

        return JsonResponse(
            {
                "error": "An error has occurred",
                "exception_type": exception_type,
                "exception_value": str(exception),
                "request_method": request.method,
                "request_url": request.get_full_path(),
                "server_time": str(datetime.datetime.now()),
            },
            status=500,
        )

