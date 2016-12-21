# 知识点

1. 通用视图概念和基本用法
2. 基于类的视图的分类、写法和使用



# 简介

## 通用试图概念
通用视图是Django为解决建站过程中的常见的呈现模式而建立的

## 通用视图使用原则
1. 代码越少越好
2. 永远不要重复代码
3. View应当只包含呈现逻辑, 不应包括业务逻辑
4. 保持view逻辑清晰简单

## Django的Class Basic View

|名字| 目的|
|-------|----------------|
| View|基本View, 可以在任何时候使用|
| RedirectView|重新定向到其他URL|
| TemplateView|显示Django HTML template|
| ListView|显示对象列表|
| DetailView|显示对象详情|
| FormView|提交From|
| CreateView|创建对象|
| UpdateView|更新对象|
| DeleteView|删除对象|
| Generic date views|显示一段时间内的对象|

## 参考文档
[代码地址：Spareibs的Github](https://github.com/spareribs/learning/tree/master/Django/Django_up/class_13)

# 实验操作

## 直接指定需要访问的主页，不需要添加导入和编写views的逻辑
```
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^index/$', IndexView.as_view(template_name='tasks.html')),
]
```

## 或者在views中指定访问主页的类【TemplateView】

先在views中定义一个子类的IndexView
```python
class IndexView(TemplateView):
    template_name = 'index.html'
```

在urls中使用
```python
from .views import IndexView
from django.views.generic import TemplateView

urlpatterns = [
    # 在view中指定访问主页的类
    url(r'^index/$', IndexView.as_view()),
]
```

## 直接重定向到其他的URL【RedirectView】
```python
urlpatterns = [
    # RedirectView跳转到百度的页面
    url(r'^redirect/$', RedirectView.as_view(url='http://baidu.com')),
]
```

## 直接使用list显示数据库的对象列表【ListView】

模板文件
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% for task in task_list %}
    <li>{{ task }}</li>
{% endfor %}
</body>
</html>
```

先在views中定义一个子类的IndexView
```python
from .models import Task
from django.views.generic import TemplateView,

class ShowTasksView(ListView):
    template_name = 'tasks.html'
    model = Task
```

在urls中使用
```python
from .views import ShowTasksView

urlpatterns = [
    # ListView:显示对象的列表
    url(r'^tasks/$', ShowTasksView.as_view()),
]
```

## 通过task_id仅显示一个task的对象【TemplateView】

模板文件
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<li>{{ task }}</li>
</body>
</html>
```

先在views中定义一个子类的DisplaySingleTaskView
```python
from .models import Task
from django.views.generic import TemplateView,

class DisplaySingleTaskView(TemplateView):
    template_name = 'single_task.html'

    def get_context_data(self, **kwargs):
        context = super(DisplaySingleTaskView, self).get_context_data(**kwargs)
        task_id = self.kwargs.get('task_id', 0)
        context['task'] = Task.objects.get(task_id=task_id)
        return context
```

在urls中使用
```python
from .views import DisplaySingleTaskView

urlpatterns = [
    # 通过task_id仅显示一个task
    url(r'^task/(?P<task_id>\d+)/$', DisplaySingleTaskView.as_view()),
]

```

## 通用视图添加对象

### 通用视图添加对象task

模板文件【add_task.html】
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" name="add" value="add">
</form>
</body>
</html>
```

模板文件【post_success.html】
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
post success
</body>
</html>
```

先创建一个Froms【froms.py】
```python
from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_id', 'name']
```

在视图中使用【views.py】
```python
from .forms import AddTaskForm

class AddTaskView(View):
    def get(self, request):
        return render(request, 'add_task.html', {'form':AddTaskForm()})

    def post(self, request):
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/success')
```

在urls中使用【urls.py】
```python
from .forms import AddPoemForm

urlpatterns = [
    # 添加task的url
    url(r'^addtask/$', AddTaskView.as_view()),
    # 添加task成功的url
    url(r'^success/$', TemplateView.as_view(template_name='post_success.html')),
]
```



### 修改通用视图可以添加对象poem

先创建一个Froms【froms.py】
```
class AddPoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['author', 'title']
```

在urls中使用【urls.py】
```python
urlpatterns = [
    # 添加task的url
    url(r'^addtask/$', AddModelView.as_view()),
    # 添加poem的url,在url中修改视图的参数
    url(r'^addpoem/$', AddModelView.as_view(form_class=AddPoemForm)),
]
```

试图模板修改成通用模板【views.py】
```python
class AddModelView(View):
    form_class = AddTaskForm
    template_name = 'add_task.html'

    def get(self, request):
        return render(request, self.template_name, {'form':self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/success')
```