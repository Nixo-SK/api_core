from rest_framework.exceptions import APIException


class InvalidRequestException(APIException):
    """Overrides APIException to provide custom message output and response code to incorrectly submitted requests."""
    status_code = 400
    default_detail = 'Invalid request data.'


class DoesNotExistException(APIException):
    """Overrides APIException to provide custom message output and response code for a situation, when there are no
    requested data found."""
    status_code = 404
    default_detail = 'Requested data does not exist.'


class DuplicateEntryException(APIException):
    """Overrides APIException to provide custom message output and response code to a submitted duplicate entry."""
    status_code = 400
    default_detail = 'Duplicate entry.'


class InternalServerErrorException(APIException):
    """Overrides APIException to provide custom message output and response code in a situations, where something goes
    wrong."""
    status_code = 500
    default_detail = 'An internal server error has occurred.'
