from django import template

register = template.Library()

@register.simple_tag
def Save_Price(Regular_Price, Special_Price):
    return Regular_Price - Special_Price

@register.simple_tag
def Product_Price(Special_Price, Quentity):
    return Special_Price * Quentity