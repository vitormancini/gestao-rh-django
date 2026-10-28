from django.db import models
from apps.funcionarios.models import Funcionario

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, verbose_name="Motivo")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT, verbose_name="Funcionario")

    def __str__(self):
        return self.motivo
