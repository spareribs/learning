# 知识点

1. mongodb简介
2. django如何集成mongodb
3. 实际操作mongodb

# 简介

## 参考文档
[window平台安装 MongoDB](http://www.runoob.com/mongodb/mongodb-window-install.html)
[代码地址：Spareibs的Github](https://github.com/spareribs/learning/tree/master/Django/Django_up/class_06)

## mongodb简介

MongoDB是基于文档(Document)的NoSQL数据库。文档是MongoDB中数据的基本单元，非常类似于关系数据库中的行(比行要复杂)。

1. database | database | 数据库
2. table | collection | 数据库表/集合
3. row | document | 数据记录行/文档
4. column | field | 数据字段/域
5. index | index | 索引
6. primary key | primary key | 主键,MongoDB自动将_id字段设置为主键

## Django如何集成mongodb

1. 最好的选择是mongoengine
2. 安装mongoengine
3. 修改setting.py
4. 建立与mongo服务器连接
5. 建立Document

## Django操作mongdb

1. 新增数据
2. 查询数据
3. 更新数据
4. 删除数据

# 实验步骤

## 安装mongoengine

```cmd
(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_06>pip install mongoengine
Collecting mongoengine
  Downloading mongoengine-0.11.0.tar.gz (352kB)
    100% |████████████████████████████████| 358kB 156kB/s
Collecting pymongo>=2.7.1 (from mongoengine)
  Downloading pymongo-3.4.0-cp35-none-win_amd64.whl (270kB)
    100% |████████████████████████████████| 276kB 235kB/s
Collecting six (from mongoengine)
  Using cached six-1.10.0-py2.py3-none-any.whl
Building wheels for collected packages: mongoengine
  Running setup.py bdist_wheel for mongoengine ... done
  Stored in directory: C:\Users\Administrator\AppData\Local\pip\Cache\wheels\fc\80\d0\3a48dab37e56de6600b07016fcb0c593afcc8926ad76b777e0
Successfully built mongoengine
Installing collected packages: pymongo, six, mongoengine
Successfully installed mongoengine-0.11.0 pymongo-3.4.0 six-1.10.0
```

## Django设置mongodb【settings.py】
```python

INSTALLED_APPS = [
    'mongoengine',
]

MONGODB_DATABASES = {
    "default": {
        "name": "test",
        "host": '127.0.0.1',
        "tz_aware": True, # 设置时区
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy'
    }
}

from mongoengine import connect
connect('test', host='127.0.0.1')
```

## Windows下面安装MangoDB

将MangoDB加入注册表，安装可以查看参考文档，安装过程略
```
C:\Program Files\MongoDB\Server\3.4\bin>mongod.exe --logpath "D:\mongodb\data\mongodb.log" --logappend --dbpath "D:\mongodb\data" --port 27017 --serviceName MongoDB --install

C:\Program Files\MongoDB\Server\3.4\bin>mongo.exe
MongoDB shell version v3.4.0
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.4.0
Server has startup warnings:
2016-12-18T18:23:53.361+0800 I CONTROL  [initandlisten]
2016-12-18T18:23:53.361+0800 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2016-12-18T18:23:53.361+0800 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2016-12-18T18:23:53.361+0800 I CONTROL  [initandlisten]
>
```

## 详细各项配置

### modules.py

```
from mongoengine import *


# Create your models here.
class Poem(Document):
    # poem
    meta = {
        # 数据库中显示的名字
        'collection': 'poem_data'
    }
    poem_id = SequenceField(required=True, primary_key=True)
    author = StringField()
    title = StringField()

    # 可以定义查询集
    @queryset_manager
    def show_newest(doc_cls, queryset):
        # 通过poem_id降序显示
        return queryset.order_by('-poem_id')
```

### views.py

```
from django.shortcuts import render, HttpResponseRedirect
from polls.models import Poem


# Create your views here.
def home(request):
    # 主页将所有的数据库数据返回
    return render(request, 'home.html', {"show_title": "所有诗词信息", "poems": Poem.objects.all()})


def add(request):
    if request.method == 'POST':
        author = request.POST.get('author', "")
        poem = Poem(author=author)
        poem.save()
        title = request.POST.get("title", "")
        poem.title = title
        # 如果添加数据库没有的数据，添加试成功的，但是这个tag是不会被保存的
        poem.tag = 'tag'
        poem.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'add.html')


def search(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        poems = Poem.show_newest(author=author)
        # 此处的查询结果poems是一个list
        return render(request, 'home.html', {"show_title": "查询结果", "poems": poems})

    else:
        return render(request, 'search.html')


def modify(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        author = request.POST.get('author', "")
        title = request.POST.get("title", "")
        poems = Poem.objects(poem_id=id)
        for poem in poems:
            poem.update(author=author, title=title)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'modify.html')


def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        poems = Poem.objects(poem_id=id)
        for poem in poems:
            poem.delete()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'delete.html')
```

### urls.py

```
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add/', views.add, name='add'),
    url(r'^search/', views.search, name='search'),
    url(r'^modify/', views.modify, name='modify'),
    url(r'^delete/', views.delete, name='delete'),
]
```