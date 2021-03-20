import json

import requests
from django.shortcuts import render
from rest_framework import viewsets, mixins
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework_jwt.views import obtain_jwt_token

from auth_.serializers import LoginSerializer
from auth_.token import get_token

User = get_user_model()


class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer

    def create(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if email is None or password is None:
            raise Exception('Введите email или пароль')
        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise Exception('Неправильный пароль!')
        except User.DoesNotExist:
            raise Exception('Пользователь не найден!')
        data = {
            "email": email,
            "password": password
        }
        token = get_token(user)
        return Response(token)