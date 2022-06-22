from rest_framework import viewsets

from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer
from.paginations import ProductPagination, ReviewPagination


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination
