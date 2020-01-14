# -*- coding: utf-8 -*-
from rest_framework import viewsets
from testing_pizza.models import PizzaMenuItem
from testing_auth.models import CustomUser
from rest_api_app.rest_classes.serializers import (
    PizzaMenuItemSerializer,
    UserSerializer,
)


class PizzaMenuItemViewSet(viewsets.ModelViewSet):
    queryset = PizzaMenuItem.objects.all()
    serializer_class = PizzaMenuItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
