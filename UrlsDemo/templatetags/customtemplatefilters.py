from django import template
register = template.Library()

def cut(value,arg):
    """
    This cut out all values of "arg" from the string!
    """
    return value.replace(arg,'')

register.filter('cut',cut)
