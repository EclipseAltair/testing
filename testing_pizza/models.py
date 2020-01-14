from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save


class Address(models.Model):
    full = models.CharField('Адрес', max_length=150)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.full


class PizzaIngredient(models.Model):
    name = models.CharField('Ингредиент', max_length=50)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class PizzaMenuItem(models.Model):
    name = models.CharField('Название', max_length=50)
    ingredients = models.ManyToManyField(PizzaIngredient, related_name='ingredients', verbose_name='Ингредиенты')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class PizzaSize(models.Model):
    LARGE = ('XL', 'Большая')
    MEDIUM = ('MD', 'Средняя')
    SMALL = ('SM', 'Маленькая')
    __all = (LARGE, MEDIUM, SMALL)

    size = models.CharField('Размер', max_length=2, choices=__all)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.size


class PizzaOrderManager(models.Manager):
    def get_queryset(self, **kwargs):
        return super(PizzaOrderManager, self).get_queryset().filter(delivered=True)


class PizzaOrder(models.Model):
    kind = models.ForeignKey(PizzaMenuItem, related_name='pizzas', verbose_name='Вид', on_delete=models.CASCADE)
    size = models.ForeignKey(PizzaSize, related_name='pizzas', verbose_name='Размер', on_delete=models.CASCADE)
    delivery = models.ForeignKey(Address, related_name='pizzas', verbose_name='Доставка', on_delete=models.CASCADE)

    extra = models.ManyToManyField(PizzaIngredient, blank=True, related_name='pizzas_extras', verbose_name='Доп.')
    exclude = models.ManyToManyField(PizzaIngredient, blank=True, verbose_name='Исключенные')
    comment = models.CharField('Комментарий', max_length=140, blank=True)

    delivered = models.BooleanField('+/-', default=False)
    date_created = models.DateTimeField('Дата создания', default=timezone.now)
    date_delivered = models.DateTimeField('Дата доставки', default=None, null=True)

    objects = models.Manager()
    delivered_manager = PizzaOrderManager()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def mark_delivered(self, commit=True):
        self.delivered = True
        self.date_delivered = timezone.now()
        if commit:
            self.save()

    def save(self, **kwargs):
        if not self.pk:
            print('Создание нового заказа!')
        else:
            print('Обновление существующего')

        super(PizzaOrder, self).save(**kwargs)

    def __str__(self):
        return 'Заказ №{}'.format(self.id)


def post_save_handler(sender, **kwargs):
    print(sender, kwargs)
    print('Заказ обновлен!')

post_save.connect(post_save_handler, sender=PizzaOrder)
