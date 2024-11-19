from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=150, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"  # Изменяет название таблицы в таблице SQLite
        verbose_name = "категорию"  # Изменяет название категории в адним-панели для единственного числа
        verbose_name_plural = "категории"  # То же для множественного числа
        ordering = ("id",) # Определяет порядок сортировки объектов модели по умолчанию

    # Изменяет отображение названий категорий в админ-панели (в списке категорий)
    def __str__(self):
        return str(self.name)


class Products(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=150, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Изображение"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Скидка"
    )
    quatity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория"
    )

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("goods:product", kwargs={"product_slug": self.slug})

    def __str__(self):
        return f"{self.name} Количество - {self.quatity}"

    def display_id(self):
        return f"id: {self.id:05}"  # :05 - Впереди id заполнится нолями, чтобы получилось 5 символов в общем

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
