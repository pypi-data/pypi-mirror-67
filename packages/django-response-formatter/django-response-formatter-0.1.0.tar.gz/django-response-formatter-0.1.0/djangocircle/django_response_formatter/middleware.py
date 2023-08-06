from rest_framework.views import exception_handler
from django.http import JsonResponse

def get_response(message="", result={}, status=True, status_code=200):
    """ common format of API response """
    return {
        "message" : message,
        "result" : result,
        "status" : status,
        "status_code" : status_code,
    }

def get_error_message(error_dict):
    """ parse the error message from the raised exception """
    field = next(iter(error_dict))
    response = error_dict[next(iter(error_dict))]
    if isinstance(response, dict):
        response = get_error_message(response)
    elif isinstance(response, list):
        response_message = response[0]
        if isinstance(response_message, dict):
            response = get_error_message(response_message)
        else:
            response = response[0]
    return response

def custom_response_exception_handler(exc, context):
    """ custom exception handler, catches the raised exception and returns the formatted response with error message """
    error_response = exception_handler(exc, context)
    if error_response is not None:
        error = error_response.data

        if isinstance(error, list) and error:
            if isinstance(error[0], dict):
                error_response.data = get_response(
                    message=get_error_message(error),
                    status_code=error_response.status_code,
                    status=False
                )

            elif isinstance(error[0], str):
                error_response.data = get_response(
                    message=error[0],
                    status_code=error_response.status_code,
                    status=False
                )

        if isinstance(error, dict):
            error_response.data = get_response(
                message=get_error_message(error),
                status_code=error_response.status_code,
                status=False
            )

    return error_response


class ResponseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if response.status_code == 500:
            response = get_response(
                message="Internal server error, please try again later", 
                status_code=response.status_code,
                status=False
            )
            return JsonResponse(response, status=response['status_code'])

        if response.status_code == 404 and "Page not found" in str(response.content):
            response = get_response(
                message="Page not found, invalid url", 
                status_code=response.status_code,
                status=False
            )
            return JsonResponse(response, status=response['status_code'])

        return response