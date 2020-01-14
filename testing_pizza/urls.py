# -*- coding: utf-8 -*-
from django.urls import path
from . import views


app_name = 'pizza'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('view/<int:pizza_order_id>/', views.view, name='view'),
    path('close/<int:pizza_order_id>/', views.close, name='close'),
    path('stats/', views.stats, name='stats'),
]
