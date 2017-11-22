from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView,
                                  DetailView,
                                  UpdateView,
                                  ListView)
from .models import Student


class StudentDetail(DetailView):
    model = Student
    template_name = 'student/student_detail.html'


class StudentList(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student/student_list.html'

class StudentWithoutResultList(LoginRequiredMixin, ListView):
    template_name = 'student/student_list.html'
    def get_queryset(self):
        return Student.objects.without_result()


class StudentCreate(LoginRequiredMixin, CreateView):
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


class StudentUpdate(LoginRequiredMixin, UpdateView):
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
