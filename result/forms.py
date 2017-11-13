from django import forms

from result.models import Result


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = '__all__'
