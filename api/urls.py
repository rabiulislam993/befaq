from django.conf.urls import url, include
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^result/', include('result.api.urls', namespace='result_api')),
    # url(r'^$', TemplateView.as_view(template_name='api/api_doc.html'), name='api_doc'),
]
