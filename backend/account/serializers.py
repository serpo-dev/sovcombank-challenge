from rest_framework import serializers

from account.models import Acc, Transaction
from users.models import User, Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'serial', 'number',)
        read_only_fields = ('user',)


class AccSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acc
        fields = ('id', 'acc_number', 'amount_in_acc', 'currency',)
        read_only_fields = ('currency',)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'acc', 'transaction_sum', 'created_at',)
        read_only_fields = ('user',)


class UserSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(read_only=True)
    accounts = AccSerializer(read_only=True, many=True)
    transactions = TransactionSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'documents', 'accounts', 'transactions',)
        read_only_fields = ('id',)


