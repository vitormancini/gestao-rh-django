from django.urls import path

from .views import (
    FuncionariosCreate,
    FuncionariosDelete,
    FuncionariosList,
    FuncionariosUpdate,
)

urlpatterns = [
    path("", FuncionariosList.as_view(), name="list_funcionarios"),
    path("editar/<int:pk>/", FuncionariosUpdate.as_view(), name="update_funcionario"),
    path("deletar/<int:pk>/", FuncionariosDelete.as_view(), name="delete_funcionario"),
    path("novo/", FuncionariosCreate.as_view(), name="create_funcionario"),
]
