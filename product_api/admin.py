from .models import (
    Product,
    Comment,
    Image,
    Tag,
    Category,
    Booking
)

from django.contrib import admin

from import_export import resources
from import_export.admin import ExportActionMixin


class ImageInstanceInline(admin.TabularInline):
    model = Image


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ("name", "price", "address", "comment_link", "show_average", "soft_delete", "owner", "created_at")


@admin.register(Product)
class ProductAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ProductResource
    list_display = ("name", "price", "address", "comment_link", "show_average", "soft_delete", "owner", "created_at")
    list_filter = ('name', 'price', 'address', 'soft_delete')
    inlines = [ImageInstanceInline]

    def comment_link(self, obj):
        from django.utils.html import format_html
        count_comments = obj.comment_set.all().count()
        url = f"/admin/product_api/comment/?product__id__exact={obj.id}"
        return format_html('<a href="{}">{} Comments </a>', url, count_comments)

    comment_link.short_description = "Comments"

    class Meta:
        ordering = ("-pk",)


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment
        fields = ("product", "user", "comment", "rating")


@admin.register(Comment)
class CommentAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = CommentResource
    list_display = ("product", "user", "comment", "rating")
    list_filter = ("product", "rating", "user")

    class Meta:
        ordering = ("product", "user")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "path", "product", "soft_delete", "created_at")
    list_filter = ('title', 'soft_delete')

    class Meta:
        ordering = ("-created_at", )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "payment", "product", "start_date", "end_date", "created_at")

    class Meta:
        ordering = ("-created_at", )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ('title',)

    class Meta:
        ordering = ("-pk",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", )
    list_filter = ('title',)

    class Meta:
        ordering = ("-pk", )
