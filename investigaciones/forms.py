from django.forms import ModelForm
from django import forms
from.models import Contenido, Comment,Denuncia
from ckeditor.widgets import CKEditorWidget
from.models import Contenido, Comment,Denuncia, Voto

class ContenidoForm(forms.ModelForm):
    contenido = forms.CharField(widget=CKEditorWidget(config_name='default'))  # Configura el CKEditorWidget

    class Meta:
        model = Contenido
        fields = ['titulo', 'descripcion', 'contenido', 'autor', 'imagen', 'ano', 'materia']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),  # Usa Textarea aquí
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.Select(attrs={'class': 'form-control'}),
            'materia': forms.Select(attrs={'class': 'form-control'}),
        }
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
class DenunciaForm(ModelForm):
    class Meta:
        model = Denuncia
        fields = ['motivo', 'content']
        widgets = {
            'motivo': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
        }
class VotoForm(ModelForm):
    class Meta:
        model = Voto
        fields = ('rating',)
        widgets = {
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            
        }
        