from urllib import request
from django import template

from carts.utils import get_user_carts
from carts.models import Cart


register = template.Library()


@register.simple_tag()
def carts_tag(request):
    return get_user_carts(request)
