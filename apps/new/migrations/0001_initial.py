# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-12-09 16:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='标题')),
                ('desc', models.CharField(default='', max_length=150, verbose_name='描述')),
                ('detail', models.TextField(verbose_name='新闻详情')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '新闻中心',
                'verbose_name_plural': '新闻中心',
            },
        ),
    ]
