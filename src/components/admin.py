from django.contrib import admin

# Register your models here.

from .models import Component
from .models import Specification

admin.site.register(Component)
admin.site.register(Specification)