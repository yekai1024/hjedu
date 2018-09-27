from django.contrib import admin
from .models import HJClass

# Register your models here.
class HJclassAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'short_url', 'long_url', 'in_use']
    actions = ['generate_html']

    def generate_html(self, request, queryset):
        for obj in queryset:
            print(obj.class_name)
        self.message_user(request, "Successfully generated class.")
    generate_html.short_description = "Generate Class"

admin.site.register(HJClass, HJclassAdmin)