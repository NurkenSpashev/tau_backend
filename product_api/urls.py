from django.urls import path, include

from .views import (
    ProductViewSet,
    CommentViewSet
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
