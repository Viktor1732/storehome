from django.template.loader import render_to_string
from django.urls import reverse
from carts.utils import get_user_carts
from carts.models import Cart


class CartMixin:
    def get_cart(self, request, product=None):

        if request.user.is_authenticated:
            query_kwargs = {"user": request.user}
        else:
            query_kwargs = {"session_key": request.session.session_key}

        if product:
            query_kwargs["product"] = product

        return Cart.objects.filter(**query_kwargs).first()

    def render_cart(self, request):
        user_cart = get_user_carts(request)
        context = {"carts": user_cart}

        referer = request.META.get("HTTP_REFERER")
        if reverse("orders:create_order") in referer:
            context["order"] = True

        return render_to_string(
            "carts/includes/included_cart.html", context, request=request
        )
