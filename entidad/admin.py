from django.contrib import admin

# Register your models here.
from .models import Pentidad

@admin.register(Pentidad)
class PentidadAdmin(admin.ModelAdmin):
    ...
