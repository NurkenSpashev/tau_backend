from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Comment, Tag, Category
from .serializers import ProductSerializer, CommentSerializer
from .paginations import ProductPagination, CommentPagination


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('owner').prefetch_related('categories', 'tags').all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'price', 'owner']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('user', 'product').all()
    serializer_class = CommentSerializer
    pagination_class = CommentPagination
