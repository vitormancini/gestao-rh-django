from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    def query_set(self):
        empresa_logada = self.request.user.funcionario.empresa

        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionariosUpdate(UpdateView):
    model = Funcionario
    fields = (
        "nome",
        "departamento",
    )


class FuncionariosDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy("list_funcionarios")


class FuncionariosCreate(CreateView):
    model = Funcionario
    fields = (
        "nome",
        "departamento",
    )

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        username = (
            funcionario.nome.split(" ")[0] + funcionario.nome.split(" ")[1]
        ).lower()
        funcionario.usuario = User.objects.create(username=username)
        funcionario.save()

        return super().form_valid(form)
