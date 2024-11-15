from django.contrib import admin
from goods.models import Categories, Products


# Такой метод не позволяет вносить изменения для отображаемого в админ-панели
# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  # Автозаполнение slug


# Регистрируем модель Products в админ-панели, с указанием настроек для отображения и редактирования.
@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    # Автоматически генерируем поле 'slug' на основе поля 'name'.
    prepopulated_fields = {"slug": ("name",)}

    # Указываем, какие поля модели будут отображаться в списке объектов на главной странице админки.
    # В данном случае это: имя продукта, количество, цена и скидка.
    list_display = ["name", "quatity", "price", "discount"]

    # Позволяем редактировать поля 'quantity', 'price' и 'discount' прямо в списке объектов (в таблице).
    list_editable = ["quatity", "price", "discount"]

    # Устанавливаем, по каким полям можно будет выполнять поиск в админке.
    # Здесь пользователи смогут искать по имени и описанию продукта.
    search_fields = ["name", "description"]

    # Добавляем фильтры в правую панель админки для быстрого поиска и фильтрации продуктов.
    # В данном случае фильтрация возможна по полям 'name' и 'category'.
    list_filter = ["name", "category"]

    # Настроим порядок и группы полей на странице редактирования.
    # Поля будут отображаться в указанном порядке:
    fields = [
        "name",
        "category",
        "description",
        "slug",
        "quatity",
        ("price", "discount"),  # Цена и скидка на одной строке
        "image",
    ]
