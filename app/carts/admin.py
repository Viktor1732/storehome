from django.contrib import admin

from carts.models import Cart


# Класс для отображения связанных объектов модели Cart в виде таблицы (вкладка) внутри формы редактирования другой модели.
class CartTabAdmin(admin.TabularInline):
    # Указываем модель, которая будет отображаться в виде инлайн-формы.
    model = Cart

    # Указываем, какие поля из модели Cart будут отображаться в таблице.
    fields = "product", "quantity"

    # Устанавливаем поля, по которым будет производиться поиск внутри инлайн-формы.
    # Пользователи смогут искать товары по полям 'product', 'quantity' и 'created_timestamp'.
    search_fields = "product", "quantity"

    # Указываем, что поле 'search_fields' будет только для чтения и не может быть отредактировано в админке.
    readonly_fields = ("search_fields",)

    # Устанавливаем, сколько пустых строк будет показано в форме инлайн. Здесь добавляется 1 дополнительная строка.
    extra = 1


@admin.register(Cart)
class CartUser(admin.ModelAdmin):
    list_display = ["user_display", "product_display", "quantity", "created_timestamp"]
    search_fields = ["user", "product", "created_timestamp"]
    list_editable = ["quantity"]
    search_fields = ["user", "product"]
    list_filter = ["user", "product__name", "created_timestamp"]


    # Метод для отображения имени пользователя в админ-панели.
    # Если есть пользователь, то отображается его имя, в случае отсутствия - "Анонимный пользователь".
    def user_display(self, obj):
        if obj.user:
            return str(obj.user)  # Возвращаем имя пользователя
        return "Анонимный пользователь"  # Если пользователь не задан, возвращаем "Анонимный пользователь"


    # Метод для отображения имени продукта в админ-панели.
    # Возвращает название продукта, связанного с объектом Cart через поле 'name'.
    def product_display(self, obj):
        return str(obj.product.name)  # Возвращаем название продукта, связанного с корзиной
