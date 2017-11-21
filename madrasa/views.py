from django.shortcuts import render
from django.views.generic import (CreateView,
                                  DetailView,
                                  UpdateView,
                                  ListView)

from .models import Madrasa


class MadrasaDetail(DetailView):
    model = Madrasa
    template_name = 'madrasa/madrasa_detail.html'

class MadrasaList(ListView):
    model = Madrasa
    template_name = 'madrasa/madrasa_list.html'

class MadrasaCreate(CreateView):
    model = Madrasa
    fields = ['name','address','is_markaz']
    template_name = 'madrasa/madrasa_create_form.html'

class MadrasaUpdate(UpdateView):
    model = Madrasa
    fields = ['name','address','is_markaz']
    template_name = 'madrasa/madrasa_create_form.html'
