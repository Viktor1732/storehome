from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from carts.utils import get_user_carts
from carts.models import Cart
from goods.models import Products


def cart_add(request):

    product_id = request.POST.get("product_id")
    product = Products.objects.get(id=product_id)

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

    user_cart = get_user_carts(request)

    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request
    )

    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)


def cart_change(request):

    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()

    cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": cart}, request=request
    )

    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)


def cart_remove(request):

    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request
    )

    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)