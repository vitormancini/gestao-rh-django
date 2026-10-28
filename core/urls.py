from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("apps.dashboard.urls")),
    path("funcionarios/", include("apps.funcionarios.urls")),
    path("empresas/", include("apps.empresas.urls")),
    path("departamentos/", include("apps.departamentos.urls")),
    path("documentos/", include("apps.documentos.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
]
