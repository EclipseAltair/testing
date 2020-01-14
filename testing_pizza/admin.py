# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import PizzaIngredient, PizzaMenuItem, PizzaSize, PizzaOrder


class PizzaIngredientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PizzaIngredient._meta.fields]

admin.site.register(PizzaIngredient, PizzaIngredientAdmin)


class PizzaMenuItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PizzaMenuItem._meta.fields]

admin.site.register(PizzaMenuItem, PizzaMenuItemAdmin)


class PizzaSizeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PizzaSize._meta.fields]

admin.site.register(PizzaSize, PizzaSizeAdmin)


class PizzaOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PizzaOrder._meta.fields]

admin.site.register(PizzaOrder, PizzaOrderAdmin)