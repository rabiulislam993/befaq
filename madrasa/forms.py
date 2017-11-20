from django import forms


class MadrasaCreateUpdateForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField()
    address = forms.CharField()
    is_markaz = forms.BooleanField()
