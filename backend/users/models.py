from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from django_rest_passwordreset.tokens import get_token_generator

from sovkom_app import settings
from users.managers import CustomUserManager


class User(AbstractUser):
    """Custom user model"""

    email = models.EmailField(_('email address'), unique=True)
    # username_validator = UnicodeUsernameValidator()
    username = None
    phone = models.CharField(_('phone number'), max_length=10, unique=True)
    role = models.CharField(max_length=20, default='client')
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Список пользователей"
        ordering = ('is_verified', 'email')


class Document(models.Model):
    """Passports users"""

    serial = models.CharField(max_length=4)
    number = models.CharField(max_length=6)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='documents')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = "Документы"
