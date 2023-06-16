# @Project:     FundConnect
# @Filename:    templatetags/custom_filters.py
# @Author:      Daksh
# @Time:        16-06-2023 04:46 pm

from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
