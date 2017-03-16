from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    # url(r'^register/$',views.register,name='register'),
    url(r'^delegation/$',views.collegedelegation,name='delegation'),
    url(r'^ip/$',views.ip,name='ip'),
    url(r'^delegate/$',views.individualdelegation,name='delegate'),
    url(r'^form_submitted/$',views.ipformsubmit,name='form_submitted'),
    url(r'^form_submitted1/$',views.indisubmit,name='form_submitted1'),
    url(r'^form_submitted2/$',views.collsubmit,name='form_submitted2'),
    url(r'^form_submitted3/$',views.consubmit,name='form_submitted3'),
    url(r'^team2/$',views.team2,name='team2'),
    url(r'^success/$',views.success,name='success'),
   
    ]
