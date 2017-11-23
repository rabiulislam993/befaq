from django import forms

from .models import Student


class StudentCreateForm(forms.ModelForm):
    # name = forms.CharField()
    class Meta:
        model = Student
        fields = ['name',
                  'father',
                  'address',
                  'madrasa',
                  'marhala',
                  'markaz',
                  'reg_year',
                  'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'father': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'madrasa': forms.Select(attrs={'class': 'form-control'}),
            'marhala': forms.Select(attrs={'class': 'form-control'}),
            'markaz': forms.TextInput(attrs={'class': 'form-control'}),
            'reg_year': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }