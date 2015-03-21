from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from models import SimpleTokenAuthModel


class SimpleTokenAuthentication(BaseAuthentication):
    """
    Simple token authentication provides ways to easily authenticate request to specific or all API views. It uses uuid4
    strings as tokens. There is a need to generate first token by a hand or a script to successfully work with views
    connected to a token lifecycle.
    """

    def authenticate(self, request):
        """
        Overrides BaseAuthentication.authenticate method. This method tries to load authentication.token from a request
        and compare it with one from a database. If submitted token is not found in a database, authentication fails,
        otherwise instance of a token is returned.
        :param request: request data
        :return: None or instance of a token based on outcome of an authentication
        """
        token = request.DATA.get('authentication.token', None)
        if not token:
            return None

        try:
            auth_token = SimpleTokenAuthModel.objects.get(token_uuid=token)
        except SimpleTokenAuthModel.DoesNotExist:
            raise AuthenticationFailed('Token not found.')

        if not auth_token.token_enabled:
            raise AuthenticationFailed('Token disabled.')

        return auth_token, None
