from django.conf.urls import url

from .views import (StudentCreate,
                    StudentDetail,
                    StudentUpdate,
                    StudentList, )

app_name = 'student'

urlpatterns = [
    url(r'add', StudentCreate.as_view(), name='student_add'),
    url(r'update/(?P<pk>\d+)/', StudentUpdate.as_view(), name='student_update'),
    url(r'list', StudentList.as_view(), name='student_list'),
    url(r'(?P<pk>\d+)/', StudentDetail.as_view(), name='student_detail'),
]
