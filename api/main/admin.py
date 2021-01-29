from django.contrib import admin
from .models import Women
# Register your models here.

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
 fields = ['name', 'age', 'dress', 'color', 'passby']