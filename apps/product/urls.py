from django.conf.urls import url, include

from .views import ProductListView, DetailView

urlpatterns = [
    url(r'^list/(?P<seriers_id>\d+)/$', ProductListView.as_view(), name='list'),
    url(r'^detail/$', DetailView.as_view(), name='product_detail')
]