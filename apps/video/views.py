from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View  # 类方法展示view

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Video, ProductSeries


class VideoListView(View):
    def get(self, request):
        all_videos = Video.objects.all()
        all_series = ProductSeries.objects.all()

        # 对视频类别筛选
        category = request.GET.get('ct', '')
        ctname = request.GET.get('ctname', '')
        if category:
            all_videos = all_videos.filter(product_series_id=int(category))

        # 对视频进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_videos, 3, request=request)

        videos = p.page(page)

        return render(request, 'video.html', {
            'videos': videos,
            'all_series': all_series,
            'ctname': ctname
        })
