from django import forms
 
class cursoformulario(forms.Form):
    nombre = forms.CharField()
    raza = forms.CharField()