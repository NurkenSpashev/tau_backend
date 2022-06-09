from django.urls import path, include

from .views import (
    ProductViewSet, 
    ReviewViewSet
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]
