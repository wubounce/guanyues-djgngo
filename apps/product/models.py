from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


class ProductSeries(models.Model):
    name = models.CharField(max_length=50, verbose_name='送料机系列名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '送料机系列'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Product(models.Model):
    product_series = models.ForeignKey(ProductSeries,on_delete=models.CASCADE, verbose_name='送料机系列')
    name = models.CharField(max_length=50, verbose_name='送料机名称')
    category = models.CharField(default='', max_length=20, verbose_name='送料机类别')
    tag = models.CharField(default='', max_length=10, verbose_name='送料机标签')
    desc = models.CharField(default='', max_length=300, verbose_name='送料机描述')
    detail = UEditorField(verbose_name="送料机详情", imagePath="product/detail/", width=700, height=300,
                 filePath="product/files/", default='')
    image = models.ImageField(default='', upload_to='product/', max_length=100, verbose_name='送料机图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '送料机'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



