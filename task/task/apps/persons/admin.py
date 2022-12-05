from django.contrib import admin

from .models import persons, depatments

admin.site.register(persons)
admin.site.register(depatments)