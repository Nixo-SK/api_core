from rest_framework.exceptions import APIException


class InvalidRequestException(APIException):
    status_code = 400
    default_detail = 'Invalid request data'


class DoesNotExistException(APIException):
    status_code = 404
    default_detail = 'Requested data does not exist'


class DuplicateEntryException(APIException):
    status_code = 400
    default_detail = 'Duplicate entry.'