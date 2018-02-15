from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'login/$', auth_views.login, name='login'),
    url(r'^register/$', views.signup, name='signup'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'showall/$', views.index, name='showall'),
    url(r'^livesearch$', views.search, name='livesearch'),
    url(r'^show/new/', views.new, name='new'),
    url(r'^show/(?P<fv_id>\w+)/$', views.detail, name='detail'),
    url(r'^show/(?P<fv_id>\w+)/edit/$', views.edit, name='edit'),
    url(r'^show/(?P<fv_id>\w+)/delete/', views.delete, name='delete'),
]
