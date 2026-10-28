from django.urls import path

from .views import (
    DepartamentoCreate,
    DepartamentoList,
    DepartamentosDelete,
    DepartamentosUpdate,
)

urlpatterns = [
    path("", DepartamentoList.as_view(), name="list_departamentos"),
    path("editar/<int:pk>/", DepartamentosUpdate.as_view(), name="update_departamento"),
    path(
        "deletar/<int:pk>/", DepartamentosDelete.as_view(), name="delete_departamento"
    ),
    path("novo/", DepartamentoCreate.as_view(), name="create_departamento"),
]
