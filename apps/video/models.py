from datetime import datetime
from django.db import models

from product.models import ProductSeries, Product
# Create your models here.
class Video(models.Model):
    product_series = models.ForeignKey(ProductSeries, on_delete=models.CASCADE, verbose_name='送料机系列')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='送料机')
    name = models.CharField(max_length=100, verbose_name='视频名称')
    url = models.CharField(default='' ,max_length=100, verbose_name='视频访问地址', null=True, blank=True)
    video = models.FileField(default='', upload_to='video/', verbose_name='视频上传')
    video_times = models.IntegerField(default=0, verbose_name='视频时长(分钟数)')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name