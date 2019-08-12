from django.conf.urls import url

from .views import VideoListView

urlpatterns = [
    url(r'^list/$', VideoListView.as_view(), name='video_list'),

]