from django.shortcuts import render
from goods.models import Products


def catalog(request):
    context = {
        "title": "StoreHome - Каталог",
    }
    return render(request, "goods/catalog.html", context=context)


def product(request):
    context = {
        "title": "StoreHome - Каталог",
    }
    return render(request, "goods/product.html", context=context)
