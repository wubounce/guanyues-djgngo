from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View  # 类方法展示view

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import News


class NewsListView(View):
    """
    新闻列表
    """

    def get(self, request):
        all_news_list = News.objects.all()

        # 对成品进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_news_list, 8, request=request)

        news_list = p.page(page)
        return render(request, 'new.html', {
            'news_list': news_list
        })


class NewsDetailView(View):
    """新闻详情"""
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)

        return render(request, 'new_detail.html', {
            'news': news
        })


from django.shortcuts import render

# Create your views here.
