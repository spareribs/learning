# coding: utf-8
# author: spareribs

import logging
from django.shortcuts import render
from django.conf import settings

logging = logging.getLogger('blog.views')


# Create your views here.

# 全局的settings文件的配置
def global_setting(request):
    print(settings.SITE_NAME)
    return {'SITE_NAME': settings.SITE_NAME,
            'SITE_DESC': settings.SITE_DESC,
            'WEIBO_SINA': settings.WEIBO_SINA,
            'WEIBO_TENCENT': settings.WEIBO_TENCENT,
            'PRO_RSS': settings.PRO_RSS,
            'PRO_EMAIL': settings.PRO_EMAIL,
            }

def index(request):
    try:
        file = open('ss.txt', 'r')
    except Exception as e:
        logging.error(e)
    return render(request, 'index.html', locals())
