from datetime import datetime

from django.db import models

# Create your models here.
class Company(models.Model):
    mobile = models.CharField(max_length=11, verbose_name='手机')
    telephone = models.CharField('座机', max_length=32)
    address = models.CharField(max_length=50, verbose_name='公司地址')
    desc = models.CharField(max_length=50, verbose_name='公司简介')
    company_intro = models.TextField(verbose_name='公司详情')
    company_website = models.URLField(max_length=32,verbose_name='公司网址', default='www.guanyues.com')

    class Meta:
        verbose_name = '公司'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '公司'


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name="轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name="访问地址")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name