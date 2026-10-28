from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("apps.dashboard.urls")),
    path("funcionarios/", include("apps.funcionarios.urls")),
    path("empresa/", include("apps.empresas.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
]
