from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.registro_hora_extra.forms import RegistroHoraExtraForm

from .models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def query_set(self):
        empresa_logada = self.request.user.funcionario.empresa

        return RegistroHoraExtra.objects.filter(empresa=empresa_logada)


class HoraExtraUpdate(UpdateView):
    model = RegistroHoraExtra
    fields = (
        "motivo",
        "horas",
    )


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy("list_hora_extra")


class RegistroHoraExtraCreateView(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):  # Injeta o usuario logado no form
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
