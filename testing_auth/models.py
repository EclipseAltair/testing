from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    favourite_pizza = models.ForeignKey(
        'testing_pizza.PizzaMenuItem', null=True, default=None, blank=True, on_delete=models.CASCADE)

    our_note = models.CharField(max_length=140, blank=True)
