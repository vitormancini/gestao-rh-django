from django.forms import ModelForm

from apps.funcionarios.models import Funcionario

from .models import RegistroHoraExtra


class RegistroHoraExtraForm(ModelForm):
    class Meta:
        model = RegistroHoraExtra
        fields = ("motivo", "funcionario", "horas")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")  # ← Extrai antes de passar ao super
        super().__init__(*args, **kwargs)
        self.fields["funcionario"].queryset = Funcionario.objects.filter(
            empresa=user.funcionario.empresa
        )
