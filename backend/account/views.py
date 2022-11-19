from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet

from account.models import Acc
from account.serializers import UserSerializer, AccSerializer
from users.models import User


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


class UsersAccount(APIView):
    """ Класс для работы с корзиной пользователя """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        acc_user = Acc.objects.filter(user_id=request.user)
        serializer = AccSerializer(acc_user, many=True)
        return Response(serializer.data)