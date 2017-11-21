from django.shortcuts import render
from django.views.generic import (CreateView,
                                  DetailView,
                                  UpdateView,
                                  ListView)
from .models import Student


class StudentDetail(DetailView):
    model = Student
    template_name = 'student/student_detail.html'


class StudentList(ListView):
    model = Student
    template_name = 'student/student_list.html'


class StudentCreate(CreateView):
    model = Student
    fields = ['name',
              'father',
              'address',
              'madrasa',
              'marhala',
              'markaz',
              'reg_year',
              'is_active']
    template_name = 'student/student_create_form.html'


class StudentUpdate(UpdateView):
    model = Student
    fields = ['name',
              'father',
              'address',
              'madrasa',
              'marhala',
              'markaz',
              'reg_year',
              'is_active']
    template_name = 'student/student_create_form.html'
