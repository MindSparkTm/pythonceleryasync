from django.contrib import admin

# Register your models here.
from .models import Color,Logs


class ColorAdmin(admin.ModelAdmin):
    list_display = ['id','color_name']


admin.site.register(Color,ColorAdmin)

class LogAdmin(admin.ModelAdmin):
    list_display = ['id','request','response']


admin.site.register(Logs,LogAdmin)

