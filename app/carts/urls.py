from django.urls import path

from carts.views import CardAddView, CartChangeView, CartRemoveView


app_name = "cart"

urlpatterns = [
    path("cart_add/", CardAddView.as_view(), name="cart_add"),
    path("cart_change/", CartChangeView.as_view(), name="cart_change"),
    path("cart_remove/", CartRemoveView.as_view(), name="cart_remove"),
]
