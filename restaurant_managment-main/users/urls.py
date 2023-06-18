from django.urls import path
from .views import home, profile, RegisterView
from django.urls import re_path


urlpatterns = [
    re_path(r'^$', home, name='index'),
    re_path(r'^profile/$', profile, name='users-profile'),
]
 