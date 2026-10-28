from django.contrib import admin
from .models import Departamento


@admin.register(Departamento)
class DepartamentosAdmin(admin.ModelAdmin):
    pass
