# coding: utf-8
# author: spareribs

import logging

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.paginator import InvalidPage, EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect
from django.conf import settings
from models import *
from django.db.models import Count
from forms import *

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
        article_list = getPage(request, Article.objects.all())
    except Exception as e:
        logging.error(e)
    return render(request, 'index.html', locals())


def archive(request):
    try:
        # 先获取用户提交的year和month信息
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        # 通过filter过滤出对应年份的数据（icontains是包含）
        article_list = getPage(request, Article.objects.filter(date_publish__icontains=year + '-' + month))
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
        article_list = getPage(request, tag_obj.article_set.all())
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

            # 获取评论信息
            comments = Comment.objects.filter(article=article).order_by('id')
            comment_list = []
            for comment in comments:
                for item in comment_list:
                    if not hasattr(item, 'children_comment'):
                        setattr(item, 'children_comment', [])
                    if comment.pid == item:
                        item.children_comment.append(comment)
                        break
                if comment.pid is None:
                    comment_list.append(comment)

            # 评论表单
            comment_form = CommentForm({'author': request.user.username,
                                        'email': request.user.email,
                                        'url': request.user.url,
                                        'article': id} if request.user.is_authenticated() else{'article': id})
        except Article.DoesNotExist:
            return render(request, 'failure.html', {'reason': '没有找到对应的文章'})
    except Exception as e:
        logging.error(e)
    return render(request, 'article.html', locals())

# 提交评论
def comment_post(request):
    try:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # 获取表单信息
            comment = Comment.objects.create(username=comment_form.cleaned_data["author"],
                                             email=comment_form.cleaned_data["email"],
                                             url=comment_form.cleaned_data["url"],
                                             content=comment_form.cleaned_data["comment"],
                                             article_id=comment_form.cleaned_data["article"],
                                             user=request.user if request.user.is_authenticated() else None)
            comment.save()
        else:
            return render(request, 'failure.html', {'reason': comment_form.errors})
    except Exception as e:
        logging.error(e)
    return redirect(request.META['HTTP_REFERER'])


# 注销
def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        print e
        logging.error(e)
    return redirect(request.META['HTTP_REFERER'])


# 注册
def do_reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                # 注册
                user = User.objects.create(username=reg_form.cleaned_data["username"],
                                           email=reg_form.cleaned_data["email"],
                                           url=reg_form.cleaned_data["url"],
                                           password=make_password(reg_form.cleaned_data["password"]), )
                user.save()

                # 登录
                user.backend = 'django.contrib.auth.backends.ModelBackend'  # 指定默认的登录验证方式
                login(request, user)
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason': reg_form.errors})
        else:
            reg_form = RegForm()
    except Exception as e:
        logging.error(e)
    return render(request, 'reg.html', locals())


# 登录
def do_login(request):
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # 登录
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend'  # 指定默认的登录验证方式
                    login(request, user)
                else:
                    return render(request, 'failure.html', {'reason': '登录验证失败'})
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason': login_form.errors})
        else:
            login_form = LoginForm()
    except Exception as e:
        logging.error(e)
    return render(request, 'login.html', locals())