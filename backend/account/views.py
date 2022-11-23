import datetime

import requests
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from account.currency_func import api_key
from account.models import Acc, Transaction
from account.permissions import IsOwnerAcc
from account.serializers import UserSerializer, AccSerializer


class RegisterUser(APIView):
    """Регистрация покупателей"""
    # throttle_classes = [AnonRateThrottle]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        if {'email', 'password', 'phone'}.issubset(request.data):
            errors = {}
            # проверяем пароль на сложность
            try:
                validate_password(request.data['password'])
            except Exception as password_error:
                error_array = []
                for item in password_error:
                    error_array.append(item)
                return JsonResponse({'Status': False, 'Errors': {'password': error_array}})
            else:
                # Проверяем уникальность имени пользователя
                request.data.update({})
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():
                    # Сохраняем пользователя
                    user = user_serializer.save()
                    user.set_password(request.data['password'])
                    user.save()
                    return JsonResponse({'Status': True},
                                        status=status.HTTP_201_CREATED)
                else:
                    return JsonResponse({'Status': False, 'Errors': user_serializer.errors})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class LoginUser(APIView):
    """Класс для авторизации пользователя"""

    # throttle_classes = [AnonRateThrottle]

    def post(self, request, *args, **kwargs):
        if {'email', 'password'}.issubset(request.data):
            user = authenticate(request, username=request.data['email'], password=request.data['password'])

            if user is not None:
                if user.is_active:
                    token, _ = Token.objects.get_or_create(user=user)
                    return Response({'Status': True, 'Token': token.key})

            return Response({'Status': False, 'Errors': 'Не удалось авторизоваться'}, status=status.HTTP_403_FORBIDDEN)
        return Response({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'},
                        status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    """Класс для работы с данными пользователя"""
    permission_classes = [IsAuthenticated]

    # throttle_classes = [AnonRateThrottle, UserRateThrottle]

    # Возвращаем все данные пользователя
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    # Изменяем данные пользователя
    def post(self, request, *args, **kwargs):
        # Если пароль есть, проверяем его
        if 'password' in request.data:
            try:
                validate_password(request.data['password'])
            except Exception as password_error:
                return Response({'Status': False, 'Error': {'password': password_error}})
            else:
                request.user.set_password(request.data['password'])

        # Проверяем остальные данные
        user_serializer = UserSerializer(request.user, data=request.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'Status': True}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Status': False, 'Errors': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UsersAccount(APIView):
    """ Класс для работы со счетами пользователя """

    permission_classes = [IsAuthenticated, IsOwnerAcc]

    # Вывод всех счетов пользователя
    def get(self, request, *args, **kwargs):
        acc_user = Acc.objects.filter(user_id=request.user)
        serializer = AccSerializer(acc_user, many=True)
        return Response(serializer.data)

    # Изменение баланса на счете
    def put(self, request, *args, **kwargs):

        if {'acc_number', 'amount_in_acc'}.issubset(request.data):
            if int(request.data['amount_in_acc']):
                try:
                    acc = Acc.objects.get(acc_number=request.data['acc_number'])
                    data = {'amount_in_acc': acc.amount_in_acc}
                    data['amount_in_acc'] += int(request.data.get('amount_in_acc'))
                    serializer = AccSerializer(acc, data=data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        return JsonResponse({'Status': True}, status=status.HTTP_201_CREATED)
                except ObjectDoesNotExist as error:
                    return JsonResponse({'Status': False, 'Errors': str(error)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({'Status': False, 'Errors': 'Не верно указаны необходимые аргументы'},
                                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'},
                                status=status.HTTP_400_BAD_REQUEST)


class UserTransaction(APIView):
    """Класс дял совершения транзакций и вывода их списка"""

    permission_classes = [IsAuthenticated, IsOwnerAcc]

    def get(self, request, *args, **kwargs):
        transaction_user = Transaction.objects.filter(user_id=request.user)
        serializer = AccSerializer(transaction_user, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        pass


def currency_period_days(request, days, source):
    """Запрос курса за период"""

    # days: Необходимо указать кол-во дней до текущей даты
    # source: Необходимо указать валюту по отношению к курсу рубля

    date_today = datetime.date.today()
    period_to_days = date_today - datetime.timedelta(days=days)

    url = f"https://api.apilayer.com/currency_data/timeframe?start_date={period_to_days}&end_date={date_today}&source={source}&currencies=RUB"

    payload = {}
    headers = {
        "apikey": api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    match response.status_code:
        case 200:
            result = response.text
            return HttpResponse(result)
        case _:
            return HttpResponse({'Status': False}, status=status.HTTP_400_BAD_REQUEST)

