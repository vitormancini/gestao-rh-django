from django.contrib import admin
from .models import Documentos


@admin.register(Documentos)
class DocumentosAdmin(admin.ModelAdmin):
    pass
