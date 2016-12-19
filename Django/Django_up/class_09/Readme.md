# 知识点

1. 什么时候需要自定义Field
2. 如何自定义Field
3. 举例


# 简介

## 什么时候需要自定义Field
Django 的官方Model里提供了很多的 Field，但是有时候还是不能满足我们的需求

## 如何自定义Field
根据需要子类化Field或者Field子类，实现序列化和反序列化

## 举例
1. 子类化Field
2. 子类化FileField

## 参考文档
[代码地址：Spareibs的Github](https://github.com/spareribs/learning/tree/master/Django/Django_up/class_09)

# 实验步骤

## 自定义一个ListField的类

【fields.py】
```python
from django.db import models
import ast

# 自定义一个ListFiled,继承与TextField这个类
class ListFiled(models.TextField):
    description = "just a listfiled"

    # 继承TextField
    def __init__(self, *args, **kwargs):
        super(ListFiled, self).__init__(*args, **kwargs)
    # 读取数据库的时候调用这个方法
    def from_db_value(self, value, expression, conn, context):
        print('from_db_value')
        if not value:
            value = []
        if isinstance(value, list):
            return value
        print('value type ', type(value))
        # 直接将字符串转换成python内置的list
        return ast.literal_eval(value)

    # 保存数据库的时候调用这个方法
    def get_prep_value(self, value):
        print("get_prep_value")
        if not value:
            return value
        print('value type ', type(value))
        return str(value)
```

【models.py】

```python
from django.db import models
from .fields import ListFiled

class ListTest(models.Model):
    labels = ListFiled()

    def __str__(self):
        return "%s " % self.labels
```
【views.py】
```python
rom django.shortcuts import render,HttpResponseRedirect
from .models import ListTest

# Create your views here.
def home(request):
    return render(request, 'home.html')

def testlist(req):
    # 存入数据库测试
    test = ListTest()
    test.labels = ["python", "django"]
    test.labels.append("allen")
    test.save()
    # 读取数据库测试
    obs = ListTest.objects.all()
    for ob in obs:
        print((ob.labels))

    return HttpResponseRedirect("/")
```
【urls.py】
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^testlist/', views.testlist, name='testlist'),
]
```

注意：数据库同步【此步骤略】

结果显示如下
```cmd
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
get_prep_value
value type  <class 'list'>
from_db_value
value type  <class 'str'>
['python', 'django', 'allen']
```

## 文件类型的FileField
【add_file.html】
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="." method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <label>addfiles:</label>
    {{ form.as_p }}
    <input type="submit" value="ok">
</form>
</body>
</html>
```

【fields.py】
```python
from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

class ContextTypeRestrictedFileField(FileField):
    def __init__(self, content_type=None, max_upload_size=None, **kwargs):
        self.content_type = content_type
        self.max_upload_size = max_upload_size
        super(ContextTypeRestrictedFileField, self).__init__(**kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContextTypeRestrictedFileField, self).clean(*args, **kwargs)
        file = data.file
        try:
            type = file.content_type
            if type != self.content_type:
                raise forms.ValidationError('pls upload right filetype')
            if file.size > self.max_upload_size:
                raise forms.ValidationError('exceed max uploadsize')
        except AttributeError:
            print("error")
            pass
        return data
```

【models.py】

```python
from django.db import models
from .fields import ContextTypeRestrictedFileField

class AddPdfFileModel(models.Model):
    name = models.CharField(max_length=100)
    file = ContextTypeRestrictedFileField(content_type='application/pdf', max_upload_size=5242880, upload_to='pdf')

    def __str__(self):
        return self.name
```
【views.py】
```python
from django.shortcuts import render
from .models import AddPdfFileModel
from .forms import AddPdfForm

def addfile(req):
    if req.method == 'POST':
        form = AddPdfForm(req.POST, req.FILES)
        if not form.is_valid():
            print(form.errors)
            return HttpResponseRedirect("/")
        name = form.cleaned_data['name']
        file = form.cleaned_data['file']
        add_pdf_model = AddPdfFileModel(name=name, file=file)
        add_pdf_model.save()
        print('success')
        return render(req, 'add_file.html', {'form': AddPdfForm()})
    else:
        return render(req, 'add_file.html', {'form':AddPdfForm()})
```


【urls.py】
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^addfile/', views.addfile, name='addfile'),
]
```

注意：数据库同步【此步骤略】

