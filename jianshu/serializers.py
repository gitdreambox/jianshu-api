#!/usr/bin/env python
# coding:utf-8

from models import ArticleList, ArticleDetail
from rest_framework import serializers

class ArticleListSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = ArticleList
        fields = ('article_title', 'article_url', 'user', 'user_url') 


class ArticleDetailSerializer(serializers.ModelSerializer): 
    """
    """
    class Meta:
        model = ArticleDetail 
        fields = ('image', 'title', 'body', 'created', 'views', 'comments', 'likes', 'tip', 'article')



