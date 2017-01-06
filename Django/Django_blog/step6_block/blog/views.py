# coding: utf-8
# author: spareribs

import logging
from django.shortcuts import render
from django.conf import settings
from models import *
from django.db.models import Count

logging = logging.getLogger('blog.views')


# Create your views here.

# 全局的settings文件的配置
def global_setting(request):
    # settings中站点基本信息的配置
    site_name = settings.SITE_NAME
    site_desc = settings.SITE_DESC
    # 广告数据
    ad_list = Ad.objects.all().order_by('-index')[:4]
    # 关于我
    weibo_sina = settings.WEIBO_SINA
    weibo_tencent = settings.WEIBO_TENCENT
    pro_rss = settings.PRO_RSS
    pro_mail = settings.PRO_EMAIL
    # 文章排行榜的数据
    # --浏览排行
    article_click_list = Article.objects.all().order_by('-click_count')[:6]
    # --评论排行
    comment_conut_list = Comment.objects.values('article').annotate(commentcount=Count('article')).order_by(
        '-commentcount')
    article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_conut_list][:6]
    # --站长推荐
    article_recommend_list = Article.objects.filter(is_recommend=1).order_by('-click_count')[:6]
    # 标签云数据
    tag_list = Tag.objects.all()
    # 文章归档
    article_list_date = Article.objects.distinct_date()[:5]
    # 友情链接
    links_list = Links.objects.all()[:6]
    return locals()


def index(request):
    try:
        article_list = Article.objects.all()
    except Exception as e:
        logging.error(e)
    return render(request, 'index.html', locals())


def archive(request):
    try:
        # 先获取用户提交的信息
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        article_list = Article.objects.filter(date_publish__icontains=year + '-' + month)
    except Exception as e:
        logging.error(e)
    return render(request, 'archive.html', locals())
