from django.conf.urls import url

from result.api.views import (ResultDetailAPIView,
                              TopStudentResultsAPIView,
                              api_home)

urlpatterns = [
    url(r'^(?P<id>\d+)/$', ResultDetailAPIView.as_view(), name='result_detail'),
    url(r'^top/$', TopStudentResultsAPIView.as_view(), name='top_results'),
    url(r'^$', api_home, name='api_home'),

]
