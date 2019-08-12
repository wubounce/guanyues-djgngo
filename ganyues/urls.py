"""ganyues URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from  django.views.generic import TemplateView
import xadmin
from django.views.static import serve  # 处理静态文件的方法

from ganyues.settings import MEDIA_ROOT
from company.views import CompanyView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^$', CompanyView.as_view(), name='index'),

    # 产品路由
    url(r'^product/', include('product.urls', namespace='product')),

    # 视频路由
    url(r'^video/', include('video.urls', namespace='video')),

    # 新闻中心路由
    url(r'^news/', include('new.urls', namespace='new')),

    # 配置上传的静态文件访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    url(r'^contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

    #富文本相关url
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
