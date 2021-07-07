from django import forms
from crispy_forms.helper import FormHelper

class ParametersForm(forms.Form):
    fin = forms.IntegerField(label='Cantidad de segundos a simular', initial=1000, min_value=0)
    min_inicio = forms.IntegerField(label='Segundo de inicio del informe', initial=0, min_value=0)
    min_fin = forms.IntegerField(label='Segundo fin del informe', initial=1000, min_value=0)
    minA = forms.IntegerField(label='Minimo puerta A', initial=20, min_value=0)
    maxA = forms.IntegerField(label='Maximo puerta A', initial=40, min_value=0)
    minB = forms.IntegerField(label='Minimo puerta B', initial=10, min_value=0)
    maxB = forms.IntegerField(label='Maximo puerta B', initial=30, min_value=0)
    minsala1A = forms.IntegerField(label='minimo de sala 1 en horario de 8 a 10', initial=120, min_value=0)
    maxsala1A = forms.IntegerField(label='maximo de sala 1 en horario de 8 a 10', initial=240, min_value=0)
    minsala1B = forms.IntegerField(label='minimo de sala 1 en horario de 10 a 13', initial=300, min_value=0)
    maxsala1B = forms.IntegerField(label='maximo de sala 1 en horario de 10 a 13', initial=180, min_value=0)
    minsala1C = forms.IntegerField(label='minimo de sala 1 en horario de 13 a 15', initial=270, min_value=0)
    maxsala1C = forms.IntegerField(label='maximo de sala 1 en horario de 13 a 15', initial=150, min_value=0)

    def __init__(self, *args, **kwargs):
        super(ParametersForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_show_labels = False
        self.helper.form_tag = False