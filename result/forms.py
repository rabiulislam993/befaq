from django import forms

from result.models import Result
from student.models import REGISTRATION_YEARS


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = '__all__'




class ResultSearchForm(forms.Form):
    reg_id = forms.IntegerField()
    reg_year = forms.MultipleChoiceField(label='Registration Year',
                                         widget=forms.CheckboxSelectMultiple,
                                         choices=REGISTRATION_YEARS)