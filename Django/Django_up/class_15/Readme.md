# 知识点

1. Restful API介绍
2. Django Restful Framework介绍
3. 实例学习

# 简介

##Rest

Rest(Representational State Transfer)表现层状态转化

> 是一种架构风格：
- 从资源角度来观察整个网络
- 每个URL代表一种资源
- 客户端通过四个http动词对后端进行操作

## Http动词
1. get 获取资源
2. post 新建一个资源
3. put 更新资源
4. delete 删除资源


## Http动词举例
1. get /poems
2. post /poems
3. get poems/id
4. put poems/id
5. delete poems/id

## 状态码

服务器向客户端返回的状态码和信息提示：
200 OK - [GET]：服务器成功返回用户请求的数据
201 CREATED - [POST/PUT]：用户新建或修改数据成功。
400 INVALID REQUEST - [POST/PUT]：用户发出的请求有错误
更多可以参考：[10 Status Code Definitions](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

## Django REST framework
一套构建restful API有效和便利的框架
安装：pip install djangorestframework

## 参考文档
[代码地址：Spareibs的Github](https://github.com/spareribs/learning/tree/master/Django/Django_up/class_15)

# 实验操作

## 简单实现Pome的get方法和post方法

定义一个serializers.ModelSerializer的子类并设置元数据 【serializers.py】
```python
from rest_framework import serializers
from .models import Poem


class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        # 制定元数据的model和fields
        model = Poem
        fields = ['author', 'title', 'type']

```

定义视图函数的操作【views.py】
```python
from rest_framework import status
from rest_framework.response import Response
from .serializers import PoemSerializer
from .models import Poem


class PoemListView(APIView):
    def get(self, request, format=None):
        poems = Poem.objects.all()
        serializer = PoemSerializer(poems, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PoemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

定义路由策略【urls.py】
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^poems/$', views.PoemListView.as_view(), name="poem_list"),
]

```

## 使用装饰器

```python

```

定义视图函数的操作【views.py】
```pyton
@api_view(['GET', 'PUT', 'DELETE'])
def poem_detail(request, pk):
    try:
        poem = Poem.objects.get(pk=pk)
    except Poem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PoemSerializer(poem)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PoemSerializer(Poem, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        poem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

定义路由策略【urls.py】
```
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^poem/(?P<pk>[0-9]+)$', views.poem_detail, name="poem_list"),
]
```