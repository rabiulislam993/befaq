from django.conf.urls import url

from result.views import result_search, result_detail, top_results


app_name = 'result'

urlpatterns = [
    url(r'^top/$', top_results, name='top_results'),
    url(r'^(?P<id>\d+)/$', result_detail, name='result_detail'),
    url(r'^$', result_search, name='result_search'),
]