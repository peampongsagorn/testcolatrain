from django.contrib import admin
from django.contrib.admin.helpers import Fieldset

from .models import Hero

#class HeroAdmin(admin.ModelAdmin):
#   field = ['id', 'name']

admin.site.register(Hero)
