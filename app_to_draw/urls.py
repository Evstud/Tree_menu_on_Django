from django.urls import re_path
from app_to_draw.views import IndexView


app_name = 'app_to_draw'

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^(.*)/$', IndexView.as_view(), name='index'),
]
