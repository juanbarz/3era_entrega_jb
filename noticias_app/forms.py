from django import forms
from .models import Categoria, Noticia, Comentario

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100)