from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.mixins import Timestamps


class UserManager(BaseUserManager):
    """
    User Manager for overriding user creating methods
    """

    def create_user(self, username, email, gender, password=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError(_('Users must have a username.'))

        if email is None:
            raise TypeError(_('Users must have an email address.'))

        if isinstance(gender, type(None)) and gender not in self.model.GENDER.GENDERS:
            raise ValueError(_('Please select gender from the given options.'))

        user = self.model(username=username, gender=gender, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, gender, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError(_('Superusers must have a password.'))

        user = self.create_user(username, email, gender, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, Timestamps):
    class GENDER:
        MALE = 'Male'
        FEMALE = 'Female'
        OTHER = 'Other'

        GENDERS = (
            (MALE, _('Male')),
            (FEMALE, _('Female')),
            (OTHER, _('Other')),
        )

    username = models.CharField(_('Username'), max_length=50, unique=True, validators=[UnicodeUsernameValidator(), ],
                                error_messages={'unique': _('User with username already exists.')},
                                help_text=_('Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.'), )
    email = models.EmailField(_('Email'), unique=True)
    gender = models.CharField(max_length=20, choices=GENDER.GENDERS)
    image = models.ImageField(_('Profile Image'), upload_to='profileimages/', blank=True)
    is_staff = models.BooleanField(_('Is staff'), default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'gender']

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
