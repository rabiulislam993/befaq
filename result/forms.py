from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class SearchResultForm(forms.Form):
    id = forms.IntegerField(label="Student's ID",
                            required=True,
                            validators=[MinValueValidator(1)],
                            widget=forms.TextInput(attrs={'class': 'form-control'}))


class AddResultForm(forms.Form):
    def __init__(self, *args, **kwargs):
        subject_list = kwargs.pop('subject_list')
        super(AddResultForm, self).__init__(*args, **kwargs)

        for i, subject in enumerate(subject_list, 1):
            self.fields['subject_{}'.format(i)] = forms.IntegerField(label=subject,
                                                                     required=True,
                                                                     validators=[MinValueValidator(0),
                                                                                 MaxValueValidator(100)],
                                                                     widget=forms.TextInput(
                                                                         attrs={'class': 'form-control'}))

    def get_results(self):
        results = {}
        for name, value in self.cleaned_data.items():
            if name.startswith('subject_'):
                results[name] = value
        return results


class ResultFilterForm(forms.Form):
    REGISTRATION_YEARS = (
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
    )
    MARHALA = [
        ('', 'All Marhala'),
        ('takmil', 'Takmil'),
        ('fazilat', 'Fazilat'),
        ('sanabia', 'Sanabia Ulia'),
        ('mutawassitah', 'Mutawassitah'),
        ('ibtedaiyah', 'Ibtedaiyah'),
        ('hifz', 'Hifzul Quran'),
        ('tazbid', 'Ilmut Tazbid wal Qirat'),
    ]

    madrasa = forms.CharField(required=False,
                              label='Madrasa',
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Name or ID'}))

    marhala = forms.ChoiceField(choices=MARHALA,
                                label='Marhala',
                                required=False,
                                widget=forms.Select(attrs={'class': 'form-control'}))

    reg_year = forms.ChoiceField(choices=REGISTRATION_YEARS,
                                 label='Reg Year',
                                 initial='2018',
                                 required=False,
                                 widget=forms.Select(attrs={'class': 'form-control'}))
