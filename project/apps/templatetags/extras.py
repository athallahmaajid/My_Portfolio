from django import template
from django.template.defaulttags import register

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def index(iterable, key):
    return iterable.index(key)

@register.filter
def divisible(num, val):
    if num == 0:
        return False
    else:
        return num % val == 0