from django.conf.urls import url, include

# from rest_framework.documentation import include_docs_urls
from .views import APIDoc


urlpatterns = [
    url(r'^$', APIDoc.as_view(), name='api_doc'),
    url(r'^result/', include('result.api.urls', namespace='api')),
    # url(r'^', include_docs_urls(title='Result Publishing API', description='RESTful API for Result')),
]

