from django import template


register = template.Library()

@register.filter
def time_format(value):
    value = int(value)
    h = '시간'
    m = '분'
    hours = int(value/60)
    minutes = int(value%60)
    
    return '%s%s %s%s'%(hours, h, minutes, m)