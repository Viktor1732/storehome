from django.shortcuts import redirect, render

from carts.models import Cart
from goods.models import Products


def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        # Ищем корзины, которые содержат данный товар для текущего пользователя
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            # Берем первую найденную корзину (она там всего одна)
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()

        else:
            # Если корзина с этим товаром не найдена, создаем новую запись в корзине с количеством товара 1
            Cart.objects.create(user=request.user, product=product, quantity=1)

    # Перенаправляем пользователя обратно на страницу, с которой он пришел
    return redirect(request.META["HTTP_REFERER"])


def cart_change(request, product_slug): ...


def cart_remove(request, product_slug): ...
