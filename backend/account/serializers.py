from rest_framework import serializers

from account.models import Acc, Transaction
from users.models import User, Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('serial', 'number',)
        read_only_fields = ('user_id',)


class AccSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acc
        fields = ('id', 'acc_number', 'amount_in_acc', 'currency')
        read_only_fields = ('id', 'user_id',)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('acc', 'transaction_sum', 'created_at')
        read_only_fields = ('user_id',)


class UserSerializer(serializers.ModelSerializer):
    document = DocumentSerializer(read_only=True, many=True)
    account = AccSerializer(read_only=True, many=True)
    transaction = TransactionSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'document', 'account', 'transaction')
        read_only_fields = ('id',)


