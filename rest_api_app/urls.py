# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework import routers
from rest_api_app.rest_classes.views import (
    UserViewSet,
    PizzaMenuItemViewSet
)


app_name = 'rest_app'
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('pizzamenuitem', PizzaMenuItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]