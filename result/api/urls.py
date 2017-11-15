from django.conf.urls import url

from result.api.views import ResultDetailAPIView, TopStudentResultsAPIView

urlpatterns = [
    url(r'^$', ResultDetailAPIView.as_view(), name='result'),
    url(r'^(?P<reg_year>\d+)/(?P<reg_id>\d+)/$', ResultDetailAPIView.as_view(), name='result_long_url'),

    url(r'^top/$', TopStudentResultsAPIView.as_view(), name='top_results'),
]