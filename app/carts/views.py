from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse

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

    else:
        carts = Cart.objects.filter(
            session_key=request.session.session_key, product=product
        )

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()

        else:
            Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=1
            )

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
    updated_quantity = cart.quantity

    user_cart = get_user_carts(request)
    context = {"carts": user_cart}
    # если реферальная страница — create_order добавить ключ orders: True для контекста
    referer = request.META.get("HTTP_REFERER")
    if reverse("orders:create_order") in referer:
        context["orders"] = True
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", context, request=request
    )

    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quantity": updated_quantity,
    }

    return JsonResponse(response_data)


def cart_remove(request):

    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)

    context = {"carts": user_cart}
    # if referer page is create_order add key orders: True to context
    referer = request.META.get("HTTP_REFERER")
    if reverse("orders:create_order") in referer:
        context["orders"] = True

    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", context, request=request
    )

    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)
