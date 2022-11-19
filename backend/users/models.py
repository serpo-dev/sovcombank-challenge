from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.db import models

from sovkom_app import settings


class User(AbstractUser):
    """Custom user model"""

    email = models.EmailField(_('email address'), unique=True)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        unique=True,
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    phone = models.CharField(_('phone number'), max_length=10, unique=True)
    role = models.CharField(max_length=20, default='client')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Список пользователей"
        ordering = ('is_verified', 'email')


class Document(models.Model):
    """Passports users"""

    serial = models.CharField(max_length=4)
    number = models.CharField(max_length=6)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='documents')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = "Документы"
