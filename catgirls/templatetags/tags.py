from django import template
from catgirls.models import *
register = template.Library()


@register.simple_tag()
def get_catgirls():
    return CatGirl.objects.all()


@register.inclusion_tag('shablons/catlist.html')
def show_catlist(sort=None):
    if sort is None:
        cats = CatGirl.objects.all()
        return {'cats': cats}
    cats = CatGirl.objects.all().order_by(sort)
    return {'cats': cats}
