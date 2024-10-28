from django.shortcuts import render
from goods.models import Products

def catalog(request):
    goods = Products.objects.all()

    context = {
        "title": "StoreHome - Каталог",
        "goods": goods}
    return render(request, "goods/catalog.html", context=context)


def product(request):
    context = {
        "title": "StoreHome - Каталог",
    }
    return render(request, "goods/product.html", context=context)
