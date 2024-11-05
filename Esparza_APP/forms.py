from django import forms
from Esparza_APP.models import Asistente

class FormAsistente(forms.ModelForm):
    class Meta:
        model = Asistente
        fields = '__all__'
