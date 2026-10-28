from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Departamento


class DepartamentoList(ListView):
    model = Departamento

    def query_set(self):
        empresa_logada = self.request.user.funcionario.empresa

        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoCreate(CreateView):
    model = Departamento
    fields = (
        "nome",
        "empresa",
    )

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()

        return super().form_valid(form)


class DepartamentosUpdate(UpdateView):
    model = Departamento
    fields = (
        "nome",
        "empresa",
    )


class DepartamentosDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy("list_departamentos")
