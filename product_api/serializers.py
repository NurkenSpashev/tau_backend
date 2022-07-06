from rest_framework import serializers
from .models import Product, Comment


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return Product.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name', read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['product', 'user', 'comment', 'rating']
