from rest_framework.exceptions import APIException


class InvalidRequestException(APIException):
    status_code = 400
    default_detail = 'Invalid request data'