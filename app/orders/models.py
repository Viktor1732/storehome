from django.db import models

from goods.models import Products
from users.models import User


# Кастомный менеджер для запросов модели OrderItem.
# Этот класс предоставляет дополнительные методы для подсчёта общей стоимости и количества товаров в заказах.
class OrderItemQueryset(models.QuerySet):

    # Метод для подсчёта общей стоимости всех товаров в заказах.
    # Возвращает сумму стоимости всех товаров (с учётом их количества).
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    # Метод для подсчёта общего количества товаров во всех заказах.
    # Если есть товары в запросе, суммирует их количество.
    # Если товаров нет, возвращает 0.
    def total_quantity(self):
        if self:
            return sum(cart.price for cart in self) 
        return 0 


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True, verbose_name="Имя пользователя")
    created_timestamp = models.TimeField(auto_now_add=True, verbose_name="Дата создания заказа")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    requires_delivery = models.BooleanField(default=False, verbose_name="Требуется доставка")
    delivery_address = models.TextField(blank=True, null=True, verbose_name="Адрес доставки")
    payment_on_get = models.BooleanField(default=False, verbose_name="Оплата при получении")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    status = models.CharField(max_length=50, default="В обработке", verbose_name="Статус заказа")

    class Meta:
        db_table = "order"
        verbose_name = "Таблица"
        verbose_name_plural = "Таблицы"

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель: {self.user.last_name} {self.user.first_name}"  


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, default=None, null=True, verbose_name="Продукт")
    name = models.CharField(max_length=150, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.TimeField(auto_now_add=True, verbose_name="Дата продажи")

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"

    # Используем кастомный менеджер для работы с запросами к модели.
    objects = OrderItemQueryset.as_manager()

    def products_price(self):
        return round(self.price * self.quantity, 2)
    
    def __str__(self):
        return f"Товар: {self.name} | Заказ № {self.order.pk}"
