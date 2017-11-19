from django import forms


class SearchResultForm(forms.Form):
    id = forms.IntegerField(label="Student's ID",
                            widget=forms.TextInput(attrs={'class': 'form-control'}))


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
                              widget=forms.TextInput(attrs={'class':'form-control',
                                                            'placeholder':'Name or ID'}))

    marhala = forms.ChoiceField(choices=MARHALA,
                                label='Marhala',
                                required=False,
                                widget=forms.Select(attrs={'class': 'form-control'}))

    reg_year = forms.ChoiceField(choices=REGISTRATION_YEARS,
                                 label='Reg Year',
                                 initial='2018',
                                 required=False,
                                 widget=forms.Select(attrs={'class': 'form-control'}))
