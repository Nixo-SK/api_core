from django.utils import timezone
from django.db import models
from uuid import uuid4


class SimpleTokenAuthModel(models.Model):
    """
    Model is intended to store a tokens used in an authentication process. This model provides information such as
    token string representation, last use and a boolean flag if a token is enabled.
    """
    token_uuid = models.CharField(max_length=36, unique=True, default=str(uuid4()))
    token_last_use = models.DateTimeField(default=timezone.now())
    token_enabled = models.BooleanField(default=True)

    def get_token(self):
        """
        Simple method to return requested token, if it is enabled. Method updates returned token last_use time along
        the way.
        :return: token if enabled or None
        """
        if self.token_enabled:
            self.token_last_use = timezone.now()
            return self
        else:
            return None

    def change_token_status(self, data):
        """
        Method, providing ways to enable or disable token.
        :param data: data containing future state of a token
        :return: True or False, based on action correctness of an input
        """
        if data.lower() == 'true':
            self.token_enabled = True
        elif data.lower() == 'false':
            self.token_enabled = False
        else:
            return False

        return True

    def is_authenticated(self):
        """
        Method is called after successful token lookup during an authentication process, granting request permission
        to proceed to a requested view.
        :return: True
        """
        return True

