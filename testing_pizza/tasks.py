# -*- coding: utf-8 -*-
from testing.celery_app import app
from testing_pizza.models import PizzaOrder


@app.task
def greet_new_orders():
    print('Добро пожловать, новый заказ!')
    return 'Приветствие новых заказов'

@app.task
def order_created(order_id):
    order = PizzaOrder.objects.get(pk=order_id)
    print('Эта задача будет делать какую-то фоновую работу')
    return 'Фоновый результат. Комментарий: {}'.format(order.comment)
