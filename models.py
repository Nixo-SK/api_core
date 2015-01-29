from django.utils import timezone
from django.db import models
from uuid import uuid4


class SimpleTokenAuthModel(models.Model):
    token_uuid = models.CharField(max_length=36, unique=True, default=str(uuid4()))
    token_last_use = models.DateTimeField(default=timezone.now())
    token_enabled = models.BooleanField(default=True)

    def get_token(self):
        if self.token_enabled:
            self.token_last_use = timezone.now()
            return self
        else:
            return None

    def change_token_status(self, data):
        if data.lower() == 'true':
            self.token_enabled = True
        elif data.lower() == 'false':
            self.token_enabled = False
        else:
            return False

        return True

    def is_authenticated(self):
        return True

