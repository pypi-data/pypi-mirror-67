from django import template

from django_error_skins.models import ErrorSkin

register = template.Library()


@register.simple_tag
def error_skin():

    return ErrorSkin.objects.filter(active=True).first()


@register.filter
def space_to_plus(value):
    return value.replace(" ", "+")
