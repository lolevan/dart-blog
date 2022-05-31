from django import template
from django.db.models import Count

from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.annotate(cnt=Count('posts')).filter(cnt__gt=0)
    return {'categories': categories, 'menu_class': menu_class}
