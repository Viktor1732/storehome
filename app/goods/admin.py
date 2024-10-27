from django.contrib import admin
from goods.models import Categories, Products


# Такой метод не позволяет вносить изменения для отображаемого в админ-панели
# admin.site.register(Categories)
# admin.site.register(Products)


# При таком способе можно производить 'тонкую' настройку в админ-панели
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  # Автозаполнение slug


@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
