from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.mixins import Timestamps


class Profile(AbstractUser, Timestamps):
    class GENDER:
        MALE = 'Male'
        FEMALE = 'Female'
        OTHER = 'Other'

        GENDERS = (
            (MALE, _('Male')),
            (FEMALE, _('Female')),
            (OTHER, _('Other')),
        )

    gender = models.CharField(max_length=20, choices=GENDER.GENDERS)
    image = models.ImageField(_('Profile Image'), upload_to='profileimages/', blank=True)

    REQUIRED_FIELDS = ['email', 'gender']

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
