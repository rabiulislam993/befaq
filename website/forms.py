from django import forms


class ResultFilterForm(forms.Form):
    madrasa = forms.CharField(required=False)
    marhala = forms.CharField(required=False)
