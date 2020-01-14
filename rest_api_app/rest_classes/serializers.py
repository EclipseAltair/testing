# -*- coding: utf-8 -*-
from rest_framework import serializers
from testing_auth.models import CustomUser
from testing_pizza.models import PizzaMenuItem, PizzaIngredient


class PizzaMenuItemSerializer(serializers.HyperlinkedModelSerializer):

    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=PizzaIngredient.objects.all())

    class Meta:
        model = PizzaMenuItem
        fields = (
            'id',
            'name',
            'ingredients',
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
            'favourite_pizza',
            'our_note',
        )

    favourite_pizza = serializers.SlugRelatedField(slug_field='name', queryset=PizzaMenuItem.objects.all())