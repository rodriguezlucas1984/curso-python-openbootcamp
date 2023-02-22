from django import forms
from directores_cine.models import Director, Pelicula


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'fecha_nacimiento': 'Fecha nac'
        }


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'
        widgets = {
            'fecha_estreno': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'fecha_estreno': 'Fecha estreno'
        }
