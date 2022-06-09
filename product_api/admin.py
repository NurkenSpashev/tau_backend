from .models import (
    Product,
    Review,
    Image
)

from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode

from import_export import resources
from import_export.admin import ExportActionMixin


class ImageInstanceInline(admin.TabularInline):
    model = Image


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ("name", "price", "address", "category", "review_link", "show_average", "soft_delete", "author", "created_at")


@admin.register(Product)
class ProductAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ProductResource
    list_display = ("name", "price", "address", "category", "review_link", "show_average", "soft_delete", "author", "created_at")
    list_filter = ('name', 'price', 'address', 'soft_delete')
    inlines = [ImageInstanceInline]

    def review_link(self, obj):
        from django.utils.html import format_html
        count_reviews = obj.review_set.all().count()
        url = f"/admin/product_api/review/?product__id__exact={obj.id}"
        return format_html('<a href="{}">{} Reviews </a>', url, count_reviews)

    review_link.short_description = "Reviews"

    class Meta:
        ordering = ("name", "author")


class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review
        fields = ("product", "user", "comment", "rating")


@admin.register(Review)
class ReviewAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ReviewResource
    list_display = ("product", "user", "comment", "rating")
    list_filter = ("product", "rating", "user")

    class Meta:
        ordering = ("product", "user")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "path", "product", "soft_delete", "created_at")
    list_filter = ('title', 'soft_delete')

    class Meta:
        ordering = ("title", )

