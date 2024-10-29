from django.shortcuts import render
from goods.models import Products


def catalog(request):
    goods = Products.objects.all()
    context = {
        "title": "StoreHome - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context=context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        "title": "StoreHome - Каталог",
        "product": product,
    }
    return render(request, "goods/product.html", context=context)
