from django import template
from goods.models import Categories


register = template.Library()


@register.simple_tag()
def categories_tag():
    return Categories.objects.all()
