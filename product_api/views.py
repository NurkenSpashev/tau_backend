from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Comment
from .serializers import ProductSerializer, CommentSerializer
from .paginations import ProductPagination, CommentPagination


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('owner').prefetch_related('categories', 'tags').all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'price', 'owner', 'average_rating']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('user', 'product').all()
    serializer_class = CommentSerializer
    pagination_class = CommentPagination
