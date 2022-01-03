from datetime import datetime
from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Account(AbstractUser):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    objects = UserManager()

    username = None
    first_name = None
    last_name = None
    date_joined = None

    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=255)
    avatar = models.FileField(_('avatar'), upload_to='accounts', default='accounts/avatar.jpg')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
