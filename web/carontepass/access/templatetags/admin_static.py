# templatetags/admin_static.py
from django.conf import settings
from django.template import Library

register = Library()

from django.templatetags.static import static

static = register.simple_tag(static)