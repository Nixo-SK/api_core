from rest_framework.serializers import ModelSerializer
from models import SimpleTokenAuthModel


class SimpleTokenAuthSerializer(ModelSerializer):
    """
    ModelSerializer preparing output for responses sent to a client. Objects retrieved from a database using
    SimpleTokenAuthModel are formatted by this serializer and passed to a Response constructor.
    """

    class Meta:
        model = SimpleTokenAuthModel
        fields = ('id', 'token_uuid', 'token_last_use', 'token_enabled')
