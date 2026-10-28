from django.db import models
from apps.funcionarios.models import Funcionario

class Documentos(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT, verbose_name="Funcionario")

    def __str__(self):
        return self.descricao
