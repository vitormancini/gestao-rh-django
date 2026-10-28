from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.PROTECT, verbose_name="Funcionario"
    )
    arquivo = models.FileField(upload_to="documentos")

    def get_absolute_url(self):
        return reverse("update_funcionario", args=[self.funcionario.id])

    def __str__(self):
        return self.descricao
