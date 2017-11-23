from django.shortcuts import reverse
from django.contrib.messages.views import SuccessMessageMixin
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


class StudentCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StudentCreateForm
    template_name = 'student/student_create_form.html'

    success_message = 'Student ID: %(id)s Successfully Created'
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            id=self.object.id,
        )

    def get_success_url(self):
        if 'add_another' in self.request.POST:
            return reverse('student:student_add')
        else:
            return reverse('student:student_detail', kwargs={'pk':self.object.id})



class StudentUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    form_class = StudentCreateForm
    template_name = 'student/student_update_form.html'

    success_message = 'Student ID: %(id)s Successfully Updated'
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            id=self.object.id,
        )