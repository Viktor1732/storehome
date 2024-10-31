from django.utils.http import urlencode
from django import template
from goods.models import Categories


register = template.Library()


@register.simple_tag()
def categories_tag():
    return Categories.objects.all()


# takes_context=True, означает, что все контекстные переменные из context (включая request) попадут в параметр: context функции chage_params
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    # Формируем словарь
    query = context["request"].GET.dict()
    # Расширяем словарь, тем что можем передать из шаблона
    query.update(kwargs)
    #urlencode - формирует готовую строку, которую можно использовать в url-адресе
    return urlencode(query)
