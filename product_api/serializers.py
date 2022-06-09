from rest_framework import serializers
from .models import Product, Review


class ProductSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return Product.objects.create(**validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name', read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ['product', 'user', 'comment', 'rating', 'product']
