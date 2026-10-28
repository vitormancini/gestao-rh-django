from django.contrib.auth.models import User
from django.db import models

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    usuario = models.OneToOneField(
        User, on_delete=models.PROTECT, verbose_name="Usuario"
    )
    departamento = models.ManyToManyField(Departamento, verbose_name="Departamento")
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.PROTECT,
        verbose_name="Empresa",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.nome
