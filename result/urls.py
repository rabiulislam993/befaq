from django.conf.urls import url

from result.views import (result_search,
                          result_detail,
                          top_results,
                          add_result,
                          select_student_to_add_result,
                          )


app_name = 'result'

urlpatterns = [
    url(r'^top/$', top_results, name='top_results'),

    url(r'^add/$', select_student_to_add_result, name='select_student_to_add_result'),
    url(r'^add/(?P<id>\d+)/$', add_result, name='add_result'),

    url(r'^(?P<id>\d+)/$', result_detail, name='result_detail'),
    url(r'^$', result_search, name='result_search'),
]