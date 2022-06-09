from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import (
    check_username,
    index,
    RegisterView
)

urlpatterns = [
    path('', index, name='index'),
    path('check/username/', csrf_exempt(check_username), name='username'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
