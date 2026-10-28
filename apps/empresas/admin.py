from django.contrib import admin
from .models import Empresa


@admin.register(Empresa)
class EmpresasAdmin(admin.ModelAdmin):
    pass
