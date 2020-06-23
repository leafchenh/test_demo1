from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'put/$', put_user_info),
    url(r'get/$', get_grade_ranking),
]
