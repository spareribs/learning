# coding: utf-8
# author: spareribs

import logging

from django.core.paginator import InvalidPage, EmptyPage, PageNotAnInteger, Paginator
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

# 定义一个分页函数
def getPage(request, article_list):
    paginator = Paginator(article_list, 3)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
        print "-------------------"
        print article_list
        print "-----------------"
    except (InvalidPage, EmptyPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list


def index(request):
    try:
        # article_list = Article.objects.all()
        article_list = getPage(request,Article.objects.all())
    except Exception as e:
        logging.error(e)
    return render(request, 'index.html', locals())


def archive(request):
    try:
        # 先获取用户提交的year和month信息
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        # 通过filter过滤出对应年份的数据（icontains是包含）
        article_list = getPage(request,Article.objects.filter(date_publish__icontains=year + '-' + month))
    except Exception as e:
        logging.error(e)
    return render(request, 'archive.html', locals())


def biaoqian(request):
    try:
        # 获取请求的tag参数
        tag_name = request.GET.get('tag', None)
        # 找到tag所对应的Tag对象
        tag_obj = Tag.objects.get(name=tag_name)
        # 使用_set通过一对多关系进行查找
        article_list = getPage(request,tag_obj.article_set.all())
    except Exception as e:
        logging.error(e)
    return render(request, 'biaoqian.html', locals())


# 文章详情
def article(request):
    try:
        # 获取文章id
        id = request.GET.get('id', None)
        try:
            # 获取文章信息
            article = Article.objects.get(pk=id)

        except Article.DoesNotExist:
            return render(request, 'failure.html', {'reason': '没有找到对应的文章'})
    except Exception as e:
        logging.error(e)
    return render(request, 'article.html', locals())


