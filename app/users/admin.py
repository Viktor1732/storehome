from django.contrib import admin
from carts.admin import CartTabAdmin
from users.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]
    search_fields = ["username", "first_name", "last_name", "email"]

    # Указываем, что в админ-панели для модели будет использоваться инлайн-форма для отображения связанных объектов.
    inlines = [CartTabAdmin, ]
    