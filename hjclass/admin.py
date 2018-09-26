from django.contrib import admin
from .models import HJClass

# Register your models here.
class HJclassAdmin(admin.ModelAdmin):
    pass

admin.site.register(HJClass, HJclassAdmin)
