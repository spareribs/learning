# coding: utf-8
# author: spareribs

import logging
from django.shortcuts import render
from django.conf import settings

logging = logging.getLogger('blog.views')


# Create your views here.

# 全局的settings文件的配置
def global_setting(request):
    # settings中站点基本信息的配置
    site_name = settings.SITE_NAME
    site_desc = settings.SITE_DESC

    weibo_sina = settings.WEIBO_SINA
    weibo_tencent = settings.WEIBO_TENCENT
    pro_rss = settings.PRO_RSS
    pro_mail = settings.PRO_EMAIL
    return locals()


def index(request):
    return render(request, 'index.html', locals())
