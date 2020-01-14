from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from testing_auth import urls as auth_urls
from testing_pizza import urls as pizza_urls
from rest_api_app import urls as rest_urls
from testing_pizza.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(auth_urls, namespace='auth_app')),
    path('pizza/', include(pizza_urls, namespace='pizza')),
    path('api/', include(rest_urls, namespace='rest_app')),
    path('', index, name='index'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls)),
    ]