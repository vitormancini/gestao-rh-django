from django.views.generic import CreateView

from .models import Documento


class DocumentosCreate(CreateView):
    model = Documento
    fields = ("descricao", "arquivo")

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        form.instance.funcionario_id = self.kwargs["funcionario_id"]
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)
