from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (CreateView,
                                  DetailView,
                                  UpdateView,
                                  ListView)

from .models import Madrasa


class MadrasaDetail(DetailView):
    model = Madrasa
    template_name = 'madrasa/madrasa_detail.html'

class MadrasaList(LoginRequiredMixin, ListView):
    model = Madrasa
    template_name = 'madrasa/madrasa_list.html'

class MadrasaCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Madrasa
    fields = ['name','address','is_markaz']
    template_name = 'madrasa/madrasa_create_form.html'

    success_message = 'Madrasa ID: %(id)s Successfully Created'
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            id=self.object.id,
        )

class MadrasaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Madrasa
    fields = ['name','address','is_markaz']
    template_name = 'madrasa/madrasa_create_form.html'

    success_message = 'Madrasa ID: %(id)s Successfully Updated'
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            id=self.object.id,
        )
