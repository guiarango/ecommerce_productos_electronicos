from django import forms

class FundadoresFormulario(forms.Form):
    nombre_completo=forms.CharField()
    historia=forms.CharField(widget=forms.Textarea)
    imagen=forms.ImageField()