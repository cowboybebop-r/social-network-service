from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.mixins import Timestamps


class Post(Timestamps):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    title = models.CharField(_('Title'), max_length=255)
    content = models.TextField(_('Content'))

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class PostRate(Timestamps):
    liked = models.BooleanField(null=True)
    liked_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.liked_post}: {self.liked}'

    class Meta:
        verbose_name = _('Post rate')
        verbose_name_plural = _('Post rates')

