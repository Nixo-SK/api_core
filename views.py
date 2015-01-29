from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from authentication import SimpleTokenAuthentication
from serializers import SimpleTokenAuthSerializer
from models import SimpleTokenAuthModel
from exceptions import InvalidRequestException


class TestAuthView(APIView):
    authentication_classes = (SimpleTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        return Response({'detail': 'hello world!'})


class AuthTokenViewSet(GenericViewSet):

    def list(self, request):
        auth_tokens = SimpleTokenAuthModel.objects.all()
        serializer = SimpleTokenAuthSerializer(auth_tokens, many=True)
        return Response(serializer.data)

    def create(self, request):
        auth_token = SimpleTokenAuthModel()
        auth_token.save()
        serializer = SimpleTokenAuthSerializer(auth_token.get_token())
        return Response(serializer.data)

    def update(self, request, pk=None):
        if pk:
            auth_token = SimpleTokenAuthModel.objects.get(pk=pk)
            token_enabled = request.DATA.get('token_enabled')
            if auth_token and token_enabled:
                if not auth_token.change_token_status(token_enabled):
                    raise InvalidRequestException()

                auth_token.save()
                return Response({'detail': 'token status changed'})

        raise InvalidRequestException()

    def delete(self, request, pk=None):
        if pk:
            auth_token = SimpleTokenAuthSerializer.objects.get(pk=pk)
            auth_token.delete()
            return Response({'detail': 'token deleted'})

        raise InvalidRequestException()
