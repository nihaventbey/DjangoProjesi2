import re
from django import template

register = template.Library()

@register.filter
def strip_images(value):
    return re.sub(r'<img[^>]+>', '', value)
