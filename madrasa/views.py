from django.contrib.auth.mixins import LoginRequiredMixin
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

class MadrasaCreate(LoginRequiredMixin, CreateView):
    model = Madrasa
    fields = ['name','address','is_markaz']
    template_name = 'madrasa/madrasa_create_form.html'

class MadrasaUpdate(LoginRequiredMixin, UpdateView):
    model = Madrasa
    fields = ['name','address','is_markaz']
    template_name = 'madrasa/madrasa_create_form.html'
