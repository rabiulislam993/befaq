from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView,
                                  DetailView,
                                  UpdateView,
                                  ListView)
from .models import Student
from .forms import StudentCreateForm

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
    form_class = StudentCreateForm
    template_name = 'student/student_create_form.html'

    def get_success_url(self):
        if 'add_another' in self.request.POST:
            return reverse('student:student_add')



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
