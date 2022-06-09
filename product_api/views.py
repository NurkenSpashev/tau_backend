from django.views.generic import TemplateView

from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from .models import Product, Review
from .permission import ProductPermission
from .serializers import ProductSerializer, ReviewSerializer


class IndexView(TemplateView):
    template_name = 'products/index.html'


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [
        ProductPermission
    ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [
        ProductPermission
    ]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

