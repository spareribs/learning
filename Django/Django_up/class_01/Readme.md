# 知识点

1. Manager基本概念
2. 简单使用默认Manager
3. 为什么要定制Manager
4. 编码定制

# 参考文档
[代码地址：Spareibs的Github](https://github.com/spareribs/learning/tree/master/Django/Django_up/class_04)

# Manager基本概念

Manager是django模型进行数据库查询操作的接口。Django 应用的每个模型都拥有至少一个管理器。

# 实验步骤

## app下面的modules.py文件先创建一个module

```python
class ToDo(models.Model):
    content = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return "%s-%d" %(self.content,self.priority)
```

## 将ToDo的module注册[app下面的admin.py]

```python
from polls.models import ToDo
admin.site.register(ToDo)
```
## 数据库同步

同步完成以后，直接随机录入数据

```cmd
(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_04_ol>python manage.py makemigrations
Migrations for 'polls':
  0006_todo.py:
    - Create model ToDo

(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_04_ol>python manage.py migrate
Operations to perform:
  Apply all migrations: auth, sessions, polls, admin, contenttypes
Running migrations:
  Applying polls.0006_todo... OK
```

## 修改url的配置

### projects的urls的配置

```python
from django.conf.urls import include

urlpatterns = [
    url(r'', include('polls.urls')),
]
```

### app的urls配置

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^todoList/', views.todoList, name="todoList")
]
```

## 设置views文件

```python
def todoList(request):
    return render(request, 'todoList.html', {"showType": "所有事件列表", "todoList": ToDo.objects.all()})
```


## 设置html模板

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<p> {{ showType }} </p>
<div>
    {% for todoItem in todoList %}
        <p>
        {{ todoItem.content }} {{ todoItem.is_done }} {{ todoItem.priority }}
        </p>
    {% endfor %}
</div>
</body>
</html>
```

---------------------

## 自定义manger

给ToDo自定义manger
```python
class ToDo(models.Model):
    content = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return "%s-%d" %(self.content,self.priority)
    
    # 这燕子修改以后，views就不能用默认的objects来调用，提示：type object 'ToDo' has no attribute 'objects'
    todolists = models.Manager()
```

修改后的views文件
```python
def todoList(request):
    return render(request, 'todoList.html', {"showType": "所有事件列表", "todoList": ToDo.todolists.all()})
```

## 过滤数据

### 使用filter方法
```
def todoList(request):
    return render(request, 'todoList.html',
                  {"showType": "所有事件列表", "todoList": ToDo.todolists.all().filter(is_done=False).filter(priority=1)})
```

### 自定义方法（未完成事件）

先自定义一个子类【modules.py】
```python
# IncompleteTodoManager是继承Manager的一个子类，返回未完成的事件的结果集
class IncompleteTodoManager(models.Manager):
    # 重载get_queryset的方法
    def get_queryset(self):
        return super(IncompleteTodoManager, self).get_queryset().filter(is_done=False)
```

在模型中实例化【modules.py】
```python
class ToDo(models.Model):
    content = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return "%s-%d" %(self.content,self.priority)

    # 这燕子修改以后，views就不能用默认的objects来调用
    todolists = models.Manager()
    # 实例化一个IncompleteTodoManager，结果集是未完成的事件数据
    incomplete = IncompleteTodoManager()
```

调用方法【views.py】
```
def todoList(request):
    return render(request, 'todoList.html', {"showType": "所有事件列表", "todoList": ToDo.incomplete.all()})
```

### 自定义方法（高优先级）

先自定义一个子类【modules.py】
```python
class HighPriorityManager(models.Manager):
    # 重载get_queryset的方法
    def get_queryset(self):
        return super(HighPriorityManager, self).get_queryset().filter(priority=1)

```

在模型中实例化【modules.py】
```python
class ToDo(models.Model):
    content = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return "%s-%d" %(self.content,self.priority)

    # 这燕子修改以后，views就不能用默认的objects来调用
    todolists = models.Manager()
    # 实例化一个IncompleteTodoManager，结果集是未完成的事件数据
    incomplete = IncompleteTodoManager()
    high = HighPriorityManager()
```

调用方法【views.py】
```
def todoList(request):
    return render(request, 'todoList.html', {"showType": "所有事件列表", "todoList": ToDo.high.all()})
```

### 一个子类同时定义两个方法

先自定义一个子类【modules.py】
```python
class ToDoManager(models.Manager):
    def incomplete(self):
        return self.filter(is_done=False)

    def high(self):
        return self.filter(priority=1)
```

在模型中实例化【modules.py】
```python
class ToDo(models.Model):
    # 实例化
    objects = ToDoManager()
```


调用方法【views.py】
```python
# 输出所有未完成的事件
def todoList(request):
    return render(request, 'todoList.html', {"showType": "所有事件列表", "todoList": ToDo.objects.incomplete()})

# 输出指定优先级的事件
def todoList(request):
    return render(request, 'todoList.html', {"showType": "所有事件列表", "todoList": ToDo.objects.high()})
```

### 通过QuerySet方法来实现

先自定义一个子类【modules.py】
```
class TodoQuerySet(models.QuerySet):
    def incomplete(self):
        return self.filter(is_done=False)

    def high(self):
        return self.filter(priority=1)

class NewTodoManager(models.Manager):
    def get_queryset(self):
        return TodoQuerySet(self.model, using=self._db)
```

在模型中实例化【modules.py】
```
class ToDo(models.Model):
    content = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return "%s-%d" %(self.content, self.priority)

    # 实例化
    objects = NewTodoManager()
```

调用方法【views.py】
```python
# 输出指定优先级的事件
def todoList(request):
    return render(request, 'todoList.html', {"showType": "所有事件列表", "todoList": ToDo.objects.all().high().})
    
# 输出所有未完成指定优先级的事件
def todoList(request):
    return render(request, 'todoList.html', {"showType": "所有事件列表", "todoList": ToDo.objects.all().high().incomplete()})
```

### 优化QuerySet方法来实现的Manger,减少all()方法的调用


先自定义一个子类【modules.py】
```
class TodoQuerySet(models.QuerySet):
    def incomplete(self):
        return self.filter(is_done=False)

    def high(self):
        return self.filter(priority=1)

class NewTodoManager(models.Manager):
    def get_queryset(self):
        return TodoQuerySet(self.model, using=self._db)

    def incomplete(self):
        return self.get_queryset().incomplete()

    def high(self):
        return self.get_queryset().high()
```

在模型中实例化【modules.py】
```
class ToDo(models.Model):
    content = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return "%s-%d" %(self.content, self.priority)

    # 实例化
    objects = NewTodoManager()
```
调用方法【views.py】
```python
# 输出指定优先级的事件
def todoList(request):
    return render(request, 'todoList.html', {"showType": "所有事件列表", "todoList": ToDo.objects).high().})
    
# 输出所有未完成指定优先级的事件
def todoList(request):
    return render(request, 'todoList.html', {"showType": "所有事件列表", "todoList": ToDo.objects.high().incomplete()})
```