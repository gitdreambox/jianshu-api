# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-23 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87URL')),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98')),
                ('body', models.TextField(null=True, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('time', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4')),
                ('views', models.PositiveIntegerField(default=0, verbose_name=b'\xe9\x98\x85\xe8\xaf\xbb\xe6\x95\xb0')),
                ('comments', models.PositiveIntegerField(default=0, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x95\xb0')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name=b'\xe5\x96\x9c\xe6\xac\xa2')),
                ('tip', models.PositiveIntegerField(default=0, verbose_name=b'\xe6\x89\x93\xe8\xb5\x8f')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ArticleList',
            fields=[
                ('article_id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name=b'ID')),
                ('article_title', models.CharField(max_length=100, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98')),
                ('article_url', models.URLField(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85URL')),
                ('user', models.CharField(max_length=100, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('user_url', models.URLField(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85URL')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='articledetail',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jianshu.ArticleList', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x91\x98\xe8\xa6\x81'),
        ),
    ]
