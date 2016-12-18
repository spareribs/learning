# 知识点

1. 不同app使用不同数据库
2. 同一app使用不同数据库


# 简介

## 参考文档
[代码地址：Spareibs的Github](https://github.com/spareribs/learning/tree/master/Django/Django_up/class_07)

## 不同app使用不同数据库
数据库路由
1. 若无指定路由，则使用默认路由方案－default,确保数据的检索和保存使用default数据库
2. 也可指定路由


## 同一app使用不同数据库

在设置数据库路由前提下，可设置不同model的元数据app_label，达到使用不同路由

# 实验步骤

## 不同app使用不同数据库

### 设置数据库【settings.py】

使用sqlite3和mysql举例
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'db1': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_advanced',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}
```

### 设置数据库路由【settings.py】

```python
DATABASES_APPS_MAPPING = {
    'polls': 'default',
    'polls2': 'db1',
}

DATABASE_ROUTERS = ['my_blog.database_app_router.DatabaseAppsRouter']
```

### 编写路由文件【database_app_router.py】

```python
from django.conf import settings


class DatabaseAppsRouter(object):
    def db_for_read(self, model, **hints):
        app_label = model._meta.app_label
        if app_label in settings.DATABASES_APPS_MAPPING:
            res = settings.DATABASES_APPS_MAPPING[app_label]
            print(res)
            return res
        return None

    def db_for_write(self, model, **hints):
        app_label = model._meta.app_label
        if app_label in settings.DATABASES_APPS_MAPPING:
            return settings.DATABASES_APPS_MAPPING[app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # 获取对应数据库的名字
        db_obj1 = settings.DATABASES_APPS_MAPPING.get(obj1._mata.app_label)
        db_obj2 = settings.DATABASES_APPS_MAPPING.get(obj2._mata.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    def db_for_migrate(self, db, app_label, model_name=None, **hints):
        if db in settings.DATABASES_APPS_MAPPING.values():
            return settings.DATABASES_APPS_MAPPING.get(app_label) == db
        elif app_label in settings.DATABASES_APPS_MAPPING:
            return False
        return None

```

### 新建一个APP，设置相关的内容

新建app【cmd】
```cmd
(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_07>python manage.py startapp polls2
```

注册【settings.py】
```python
INSTALLED_APPS = [
    'polls2',
]

```

模板【models.py】
```
from django.db import models

# Create your models here.
class Poem(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
```

路由【urls.py】
```
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^polls2/poemlist2', views.poemlist2, name='poemlist2'),
]
```

视图【views.py】
```
from django.shortcuts import render
from .models import Poem


# Create your views here.
def poemlist2(req):
    return render(req, 'poemlist2.html', {'poems': Poem.objects.all()})
```

### 数据库同步

```cmd
(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_07>python manage.py makemigrations
Migrations for 'polls2':
  0001_initial.py:
    - Create model Poem
(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_07>python manage.py migrate --database db1
Operations to perform:
  Apply all migrations: polls, admin, polls2, auth, contenttypes, sessions
Running migrations:
  Applying polls2.0001_initial... OK

(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_07>python manage.py migrate
Operations to perform:
  Apply all migrations: contenttypes, auth, sessions, polls, admin, polls2
Running migrations:
  Applying polls.0007_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django... OK
  Applying polls2.0001_initial... OK

(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_07>python manage.py runserver
Performing system checks...
```

----------
按照上述步骤操作完成以后，polls就是用sqlite3数据库，polls2就使用mysql数据库。
同理，mangodb数据库也是可以这样子使用的


### 数据库配置【settings.py】

```
from mongoengine import connect
connect('test', host='127.0.0.1')
```

### 新建一个APP，设置相关的内容

新建app【cmd】
```cmd
(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_07>python manage.py startapp polls3
```

注册【settings.py】
```python
INSTALLED_APPS = [
    'polls3',
]

```

模板【models.py】
```
from mongoengine import *

class Poem(Document):
    meta = {
        'collection':'poem_data'
    }
    poem_id = SequenceField(required=True, primary_key=True)
    author = StringField()
    title = StringField()
```

路由【urls.py】
```
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^polls3/poemlist3', views.poemlist3, name="poemlist3")
]
```

视图【views.py】
```
from django.shortcuts import render

from .models import Poem


# Create your views here.
def poemlist3(request):
    return render(request, 'poemlist3.html', {"show_title": "所有诗词信息", "poems": Poem.objects.all()})
```

### 数据库同步
此处class_06已经给数据库写入数据,所以不需要同步数据库

### 访问的方法
http://127.0.0.1:8000/ 访问到的是polls这个app，使用的是sqlite3数据库
http://127.0.0.1:8000/polls2/poemlist2 访问到的是polls2这个app，使用的是mysql数据库
http://127.0.0.1:8000/polls3/poemlist3 访问到的是polls3这个app，使用的是mangodb数据库

## 同一个app下面使用不同数据库的方法

### 修改app_label【models.py】
```python
class Book2(models.Model):
    author = models.CharField(max_length=1024, blank=True, null=True)
    title = models.CharField(max_length=1024)

    class Meta:
        app_label = 'polls2'
```

### 修改视图函数 
```python
from polls.models import ToDo, Poem, Book2

# Create your views here.
def home(request):
    return render(request, 'home.html', {'poems': Poem.objects.all(), 'book2': Book2.objects.all()})
```