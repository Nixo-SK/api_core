from rest_framework.serializers import ModelSerializer
from models import SimpleTokenAuthModel


class SimpleTokenAuthSerializer(ModelSerializer):

    class Meta:
        model = SimpleTokenAuthModel
        fields = ('id', 'token_uuid', 'token_last_use', 'token_enabled')
