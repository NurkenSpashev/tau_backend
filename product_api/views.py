from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer
from .paginations import ProductPagination, ReviewPagination


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('owner').all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'price', 'owner', 'average_rating']


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related('user', 'product').all()
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination
