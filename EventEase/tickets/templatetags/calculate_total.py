from django import template
register=template.Library()

@register.simple_tag
def calculate_total(ticket_price,quantity):
    return ticket_price*quantity