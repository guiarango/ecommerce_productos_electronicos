from django import forms

class MessageForm(forms.Form):
    nombre_completo=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField(widget=forms.Textarea)
