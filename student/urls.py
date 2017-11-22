from django.conf.urls import url

from .views import (StudentCreate,
                    StudentDetail,
                    StudentUpdate,
                    StudentList,
                    StudentWithoutResultList,)

app_name = 'student'

urlpatterns = [
    url(r'^add$', StudentCreate.as_view(), name='student_add'),
    url(r'^update/(?P<pk>\d+)/$', StudentUpdate.as_view(), name='student_update'),
    url(r'^list$', StudentList.as_view(), name='student_list'),
    url(r'^without_result$', StudentWithoutResultList.as_view(), name='student_without_result'),
    url(r'^(?P<pk>\d+)/$', StudentDetail.as_view(), name='student_detail'),
]
