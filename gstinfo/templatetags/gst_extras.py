import datetime
from django import template

register = template.Library()

@register.simple_tag
def current_date(format_string):
	return datetime.datetime.now().strftime(format_string)