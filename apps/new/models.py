from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


class News(models.Model):
    title = models.CharField(default='', max_length=50, verbose_name='标题')
    desc = models.CharField(default='', max_length=150, verbose_name='描述')
    detail = UEditorField(verbose_name="新闻详情", imagePath="news/images/", width=700, height=300,
                              filePath="news/files/", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '新闻中心'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title