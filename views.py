from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from authentication import SimpleTokenAuthentication
from serializers import SimpleTokenAuthSerializer
from models import SimpleTokenAuthModel
import exceptions as core_exceptions


class TestAuthView(APIView):
    """Simple APIView, providing way to test correctness of an authentication."""
    authentication_classes = (SimpleTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        """Method returns sample data, after successful authentication of a request."""
        return Response({'detail': 'hello world!'})


class AuthTokenViewSet(GenericViewSet):
    """An API generic view set providing actions to list, create, update and delete tokens."""
    authentication_classes = (SimpleTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def list(self, request, pk):
        """
        Method, responding to a GET request, lists a specific token stored in a database whenever an id is provided.
        Otherwise list of all tokens is returned in a response.
        :param request: request data
        :param pk: an unique identifier of a token
        :return: rest_framework.response.Response containing serialized data
        """
        if pk is not None:
            try:
                auth_token = SimpleTokenAuthModel.objects.get(pk=pk)
                serializer = SimpleTokenAuthSerializer(auth_token)
            except SimpleTokenAuthModel.DoesNotExist:
                raise core_exceptions.DoesNotExistException()
        else:
            auth_tokens = SimpleTokenAuthModel.objects.all()
            serializer = SimpleTokenAuthSerializer(auth_tokens, many=True)

        return Response(serializer.data)

    def create(self, request):
        """
        Method, responding to a POST request, creates new token to be used during and authentication process.
        :param request: request data
        :return: rest_framework.response.Response containing serialized data
        """
        auth_token = SimpleTokenAuthModel()
        auth_token.save()
        serializer = SimpleTokenAuthSerializer(auth_token.get_token())
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """
        Method, responding to a PUT request, updates status of a specific token, which in turn determines if a token is
        disallowed or allowed for use.
        :param request: request data
        :param pk: an unique identifier of a token
        :return: rest_framework.response.Response containing serialized data
        """
        token_enabled = request.DATA.get('token_enabled', None)

        if not pk:
            raise core_exceptions.InvalidRequestException('Unique identifier (id) is missing in a request URI.')
        elif not token_enabled:
            raise core_exceptions.InvalidRequestException('Token status not found in a request.')

        try:
            auth_token = SimpleTokenAuthModel.objects.get(pk=pk)
        except SimpleTokenAuthModel.DoesNotExist:
            raise core_exceptions.DoesNotExistException()

        if not auth_token.change_token_status(token_enabled):
            raise core_exceptions.InvalidRequestException()

        auth_token.save()
        serializer = SimpleTokenAuthSerializer(auth_token.get_token())
        return Response(serializer.data)

    def delete(self, request, pk=None):
        """
        Method, responding to a DELETE request, deletes a specific token.
        :param request: request data
        :param pk: an unique identifier of a token
        :return: rest_framework.response.Response containing serialized data
        """
        if not pk:
            raise core_exceptions.InvalidRequestException('Unique identifier (id) is missing in a request URI.')

        try:
            auth_token = SimpleTokenAuthModel.objects.get(pk=pk)
            auth_token.delete()
        except SimpleTokenAuthModel.DoesNotExist:
            raise core_exceptions.DoesNotExistException()

        return Response({'deleted': True})
