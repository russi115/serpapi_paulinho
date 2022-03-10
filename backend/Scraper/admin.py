from django.contrib import admin
from .models import data

class DataAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'link', 'displayed_link')

# Register your models here.

admin.site.register(data, DataAdmin)
