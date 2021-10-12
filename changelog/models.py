from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.mixins import Timestamps


class RequestLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_request_logs')
    last_request = models.DateTimeField(_('Last request'), auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.last_request}'
