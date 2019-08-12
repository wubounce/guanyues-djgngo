from django.conf.urls import url

from .views import NewsListView, NewsDetailView

urlpatterns = [
    url(r'^list/$', NewsListView.as_view(), name='new_list'),
    url(r'^detail/(?P<news_id>\d+)/$', NewsDetailView.as_view(), name='new_detail'),

]