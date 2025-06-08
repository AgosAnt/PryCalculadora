
from django import forms

METHOD_CHOICES = (
    ('biseccion', 'Bisección'),
    ('newton', 'Newton-Raphson'),
    ('newton_mod', 'Newton-Raphson Modificado'),
)

class RootForm(forms.Form):
    funcion = forms.CharField(label='Función polinómica (ej. x**3 - 4*x - 9)', max_length=200)
    metodo = forms.ChoiceField(label='Método', choices=METHOD_CHOICES)
    a = forms.FloatField(label='Extremo a', required=False)
    b = forms.FloatField(label='Extremo b', required=False)
    x0 = forms.FloatField(label='Valor inicial x0', required=False)
    tolerancia = forms.FloatField(label='Tolerancia', initial=1e-6)
    max_iter = forms.IntegerField(label='Máximo de iteraciones', initial=50)
