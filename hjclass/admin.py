from django.contrib import admin
from .models import HJClass

# Register your models here.
class HJclassAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'short_url', 'long_url', 'in_use']

admin.site.register(HJClass, HJclassAdmin)