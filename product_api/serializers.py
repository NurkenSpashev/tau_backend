from rest_framework import serializers
from .models import Product, Comment, Tag, Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title', 'pk')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    categories = CategorySerializer(read_only=True, many=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        product = Product.objects.create(**validated_data)
        categories = self.context['request'].data.get('categories')
        tags = self.context['request'].data.get('tags')
        for tag in tags:
            if Tag.objects.filter(pk=tag['pk']).exists():
                product.tags.add(Tag.objects.get(pk=tag['pk']))
        for category in categories:
            if Category.objects.filter(pk=category['pk']).exists():
                product.categories.add(Category.objects.get(pk=category['pk']))

        return product


class CommentSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name', read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['product', 'user', 'comment', 'rating']
