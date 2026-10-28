from django.urls import path

from .views import DocumentosCreate

urlpatterns = [
    # path("", DepartamentoList.as_view(), name="list_departamentos"),
    # path(
    #     "deletar/<int:pk>/", DepartamentosDelete.as_view(), name="delete_departamento"
    # ),
    path(
        "novo/<int:funcionario_id>", DocumentosCreate.as_view(), name="create_documento"
    ),
]
