# 知识点

1. 概念
2. 如何监听信号
3. Django内置信号
4. 自定义信号
5. 使用Django内置信号


# 概念
Django 提供一个“信号分发器”，允许解耦的应用在框架的其它地方发生操作时会被通知到。
也就是说在特定事件发生时，可以发送一个信号去通知注册了这个信号的一个或者多个回调，在回调里进行逻辑处理。

## 如何监听信号
拥有一个Signal实例
信号回调
将信号回调绑定到Signal实例
在特定事件中Signal发送信号

## Django内置信号
django.db.models.signals.pre_save & post_save在模型 save()方法调用之前或之后发送。
django.db.models.signals.pre_delete & post_delete在模型delete()方法或查询集的delete() 方法调用之前或之后发送。
django.core.signals.request_started & request_finishedDjango建立或关闭HTTP 请求时发送。


## 参考文档
[代码地址：Spareibs的Github](https://github.com/spareribs/learning/tree/master/Django/Django_up/class_16)

# 实验操作

## 自定义信号

### 注册信号
【signal.py】

```python
from django.dispatch import Signal, receiver

signalAllen = Signal(providing_args=['allen'])

@receiver(signalAllen)
def signal_callback(sender, **kwargs):
    print(sender, kwargs)
    print('signal_callback called')

# 注册，或者使用装饰器注册
# signalAllen.connect(signal_callback)

# 可以定义多个
@receiver(signalAllen)
def signal_callback1(sender, **kwargs):
    print(sender, kwargs)
    print('signal_callback1 called')
```

【urls.py】
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.index),
]
```

【views.py】
```python
from . import signals
# Create your views here.

def index(request):
    signals.signalAllen.send(sender=None, allen='test')
    return render(request, template_name='index.html')
```

### 删除信号

【urls.py】
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^disconnect/$', view=views.disconnect_signal),
]
```

【views.py】
```python
def disconnect_signal(request):
    signals.signalAllen.disconnect(signals.signal_callback)
    return render(request, template_name='index.html')
```

## Django 内置信号

### 简单使用
【views.py】
```
from django.shortcuts import render
from .models import Poem, Task
# Create your views here.

def modify(request):
    poem = Poem.objects.get(pk=1)
    poem.title = '1'
    # 会发送两个信号pre_save和post_save
    poem.save()

    task = Task.objects.get(pk=1)
    task.name = '1'
    task.save()

    return render(request, template_name='index.html')
```
【urls.py】
```
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^modify/$', view=views.modify),
]
```
【singals.py】
```
from django.db.models.signals import pre_save, post_save

@receiver(pre_save)
def pre_save_callback(sender, **kwargs):
    print('pre_save_callback')


@receiver(post_save)
def post_save_callback(sender, **kwargs):
    print('post_save_callback')
```

### 指定信号
【views.py】
```
from django.shortcuts import render
from .models import Poem, Task
# Create your views here.

def modify(request):
    poem = Poem.objects.get(pk=1)
    poem.title = '1'
    # 会发送两个信号pre_save和post_save
    poem.save()

    task = Task.objects.get(pk=1)
    task.name = '1'
    task.save()

    return render(request, template_name='index.html')
```
【urls.py】
```
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^modify/$', view=views.modify),
]
```
【singals.py】
```
from django.db.models.signals import pre_save, post_save
from .models import Poem, Task

@receiver(pre_save, sender=Poem)
def pre_save_callback(sender, **kwargs):
    print('pre_save_callback', sender, kwargs)


@receiver(post_save, sender=Task)
def post_save_callback(sender, **kwargs):
    print('post_save_callback', sender, kwargs)
```