from django.conf.urls import url

from .views import (MadrasaCreate,
                    MadrasaDetail,
                    MadrasaUpdate,
                    MadrasaList, )

app_name = 'madrasa'

urlpatterns = [
    url(r'add', MadrasaCreate.as_view(), name='madrasa_add'),
    url(r'update/(?P<pk>\d+)/', MadrasaUpdate.as_view(), name='madrasa_update'),
    url(r'list', MadrasaList.as_view(), name='madrasa_list'),
    url(r'(?P<pk>\d+)/', MadrasaDetail.as_view(), name='madrasa_detail'),
]
