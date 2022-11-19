from django.core.validators import MinValueValidator
from django.db import models

from account.currencies_choices import CURRENCIES_CHOICES
from sovkom_app import settings


class Acc(models.Model):
    """Accounts for users"""

    acc_number = models.CharField(max_length=25,unique=True, verbose_name='Номер счета')
    currency = models.CharField(max_length=3, choices=CURRENCIES_CHOICES, default='RUB', verbose_name='Валюта')
    amount_in_acc = models.IntegerField(validators=[MinValueValidator(0)], default=0, verbose_name='Сумма на счете')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='accounts')

    class Meta:
        verbose_name = 'Счет пользователя'
        verbose_name_plural = "Счета пользователей"


class Transaction(models.Model):
    """Transactions for acc. users"""

    created_at = models.DateTimeField(auto_now_add=True)
    transaction_sum = models.IntegerField(verbose_name='Сумма транзакции')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    acc = models.ForeignKey(Acc, on_delete=models.CASCADE, related_name='transactions')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = "Транзакции"
