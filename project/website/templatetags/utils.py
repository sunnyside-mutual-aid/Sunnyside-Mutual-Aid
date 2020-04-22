from django import template

from website.models import Page


register = template.Library()


@register.simple_tag
def get_pages():
    return Page.objects.filter(published=True)
