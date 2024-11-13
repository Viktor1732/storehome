from django import template

from carts.models import Cart


register = template.Library()


@register.simple_tag()
def carts_tag(self):
    if self.user.is_authenticated:
        return Cart.objects.filter(user=self.user)
