from rest_framework import permissions


class ProductPermission(permissions.DjangoModelPermissions):
    authenticated_users_only = False
    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class ProductOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, product_obj):
        return product_obj.owner.id == request.user.id
