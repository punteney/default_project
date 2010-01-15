from django.contrib.flatpages.models import FlatPage
from django import template
from templatetag_sugar.register import tag
from templatetag_sugar.parser import Name, Variable, Constant, Optional, Model

register = template.Library()


@tag(register, [Optional([Constant("as"), Name()])])
def set_flatpage(context, asvar=None):
    pages = FlatPage.objects.filter(url__exact=context['request'].path)
    if pages:
        if asvar:
            context.dicts[-1][asvar] = pages[0]
        else:
            context['flatpage'] = pages[0]
    return ''
