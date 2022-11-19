from django.contrib import admin
from account.models import Acc, Transaction


@admin.register(Acc)
class AccAdmin(admin.ModelAdmin):
    list_display = ('acc_number', 'currency', 'amount_in_acc', 'user_id')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'acc_id', 'transaction_sum', 'created_at')