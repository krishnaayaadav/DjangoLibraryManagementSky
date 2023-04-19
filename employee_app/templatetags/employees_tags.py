from django import template
from employee_app.models import Employee

register = template.Library()

from employee_app.forms import SearchForm


@register.inclusion_tag('emp_app/search_form.html')
def search_form():
   form = SearchForm()
   return {'form': form}
   