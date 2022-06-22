from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Client profile
    path('client/', include(('client.urls', 'client'), namespace='client')),

    # ProductApi
    path('api/v2', include(('product_api.urls', 'product_api'), namespace='product_api')),

    # AuthenticationApi
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
