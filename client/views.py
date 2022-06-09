from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.utils.translation import gettext_lazy as _
from rest_framework import status
import json


# Create your views here.

def index(request):
    pass


def check_username(request):
    json_data = json.loads(request.body)
    username = json_data.get('username', None)
    if username is not None:
        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {'message': _(f'{username} user already exists')},
                status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
            )

        return JsonResponse({'message': True}, status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

