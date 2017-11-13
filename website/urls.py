from django.conf.urls import url

from website import views


app_name = 'website'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^register_new_student/$', views.register_student, name='register_student'),
    url(r'^student_detail/(?P<reg_id>\d+)/(?P<reg_year>\d+)/$', views.student_detail, name='student_detail'),
    url(r'^student_detail/$', views.student_detail, name='student_detail_get'),
    # url(r'^student_update/(?P<reg_id>\d+)/(?P<reg_year>\d+)/$', views.student_update, name='student_update'),

    # url(r'^add_result/$', views.add_result, name='add_result'),
    # url(r'^result_update/(?P<reg_id>\d+)/(?P<reg_year>\d+)/$', views.result_update, name='result_update'),
    url(r'^top_results/$', views.top_results, name='top_results'),
]