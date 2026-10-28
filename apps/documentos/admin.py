from django.contrib import admin

from .models import Documento


@admin.register(Documento)
class DocumentosAdmin(admin.ModelAdmin):
    pass
