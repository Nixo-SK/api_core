from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from models import SimpleTokenAuthModel


class SimpleTokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.DATA.get('authentication.token')
        if not token:
            return None

        try:
            auth_token = SimpleTokenAuthModel.objects.get(token_uuid=token)
        except SimpleTokenAuthModel.DoesNotExist:
            raise AuthenticationFailed('Token not found.')

        if not auth_token.token_enabled:
            raise AuthenticationFailed('Token disabled.')

        return auth_token, None
