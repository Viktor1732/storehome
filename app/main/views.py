from django.shortcuts import render, HttpResponse


def index(request):
    context = {"title": "StoreHome - Главная", "content": "Магазин мебелеи StoreHome"}

    return render(request, "main/index.html", context=context)


def about(request):
    context = {
        'title': 'StoreHome - О Нас!',
        'content': 'StoreHome - Магазин для Всех!',
        'text_on_page': 'Наш магазин действительно хорош! Мы крутые ребята!'
    }

    return render(request, 'main/about.html', context=context)