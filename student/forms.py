from django import forms

from student.models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name',
                  'father',
                  'madrasa',
                  'marhala',
                  'reg_year',]


