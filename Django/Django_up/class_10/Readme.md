# 知识点

1. 定制UserAdmin
2. 定制ModelAdmin



# 简介

## 参考文档
[代码地址：Spareibs的Github](https://github.com/spareribs/learning/tree/master/Django/Django_up/class_10)


# 实验步骤

## 简单测试

先定义好自己的模型【models.py】
```python
from django.db import models

# Create your models here.

class Poem(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "%s" % self.title
```

将Poem的models注册到模型中【admin.py】
这样可以增删查改Pome中的内容
```python
from django.contrib import admin
from .models import Poem

admin.site.register(Poem)
```

## 中文显示【settings】
注意：google浏览器不行，但是firefox浏览器是可以的
```python
MIDDLEWARE_CLASSES = [
    'django.middleware.locale.LocaleMiddleware',
]
```

## 定制自带的UserAdmin
```python
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class MyUserAdmin(UserAdmin):
    # 显示在管理页面的字段
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    # 定制过滤器
    list_filter = ('is_staff',)
    # 可查询字段
    search_fields = ('last_name',)

# 需要将User取消注册，然后再注册到MyUserAdmin里面
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
```

## 定制自定义的Pome
```
class PoemModelAdmin(admin.ModelAdmin):
    # 显示在管理页面的字段
    list_display = ['title', 'timestamp', 'author']
    # 可以修改内容的链接
    list_display_links = ['author']
    # 可以查询的字段，显示搜索框
    search_fields = ['title']
    # 可直接编辑的字段（但是不能同时可连接可编发来）
    list_editable = ['title']
    # 定制过滤器
    list_filter = ['author']
    class Meta:
        model = Poem
admin.site.register(Poem, PoemModelAdmin)
```

## 自定义模板显示

添加自定义模板【cahnge_form.html】
```html
{% extends "admin/change_form.html" %}

{% block form_top %}
    <!--加入提示性的语句-->
    <p>注意:不要将作者和标题写错哦!</p>
{% endblock %}
```

在admin中使用【admin.py】
```python
class PoemModelAdmin(admin.ModelAdmin):
    # 显示在管理页面的字段
    list_display = ['title', 'timestamp', 'author']
    # 可以修改内容的链接
    list_display_links = ['author']
    # 可以查询的字段，显示搜索框
    search_fields = ['title']
    # 可直接编辑的字段（但是不能同时可连接可编发来）
    list_editable = ['title']
    # 定制过滤器
    list_filter = ['author']
    
    # 自定义模板
    change_form_template = 'change_form.html'

    class Meta:
        model = Poem
admin.site.register(Poem, PoemModelAdmin)
```

## 可自定义的模板，查看源码【option.py】
```
    # Custom templates (designed to be over-ridden in subclasses)
    add_form_template = None
    change_form_template = None
    change_list_template = None
    delete_confirmation_template = None
    delete_selected_confirmation_template = None
    object_history_template = None
```

