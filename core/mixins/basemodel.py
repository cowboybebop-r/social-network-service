from django.db import models
from django.utils.translation import gettext_lazy as _


class Timestamps(models.Model):
    create_at = models.DateTimeField(_('Created'), auto_now_add=True, blank=True, null=True)
    update_at = models.DateTimeField(_('Updated'), auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True
