from django.urls import path

from carts.views import CardAddView, cart_change, cart_remove


app_name = "cart"

urlpatterns = [
    path("cart_add/", CardAddView.as_view(), name="cart_add"),
    path("cart_change/", cart_change, name="cart_change"),
    path("cart_remove/", cart_remove, name="cart_remove"),
]
