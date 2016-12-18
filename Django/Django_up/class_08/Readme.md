# 知识点

1. 如何自定义表单
2. 表单验证

# 简介

## 参考文档
[代码地址：Spareibs的Github](https://github.com/spareribs/learning/tree/master/Django/Django_up/class_08)

# 实验步骤

## 非自定义表单
### 简单的Form处理方法

```html
<h1>最原始的Form：全手工写</h1>
<form action="." method="post">
    {% csrf_token %}
    <label>增加诗词信息: </label>
    author:<input id="author" type="text" name="author" value="{[ author ]}">
    title:<input id="title" type="text" name="title" value="{[ title ]}">
    <input type="submit" value="OK">
</form>
```

```python
from django.shortcuts import render, HttpResponseRedirect
from .models import Poem


def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if not form.is_valid():
            print('invalid')
            return render(request, 'add_poem.html', {'form': AddForm()})
        author = form.cleaned_data['author']
        title = form.cleaned_data['title']
        poem = Poem(author=author, title=title)
        poem.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'add_poem.html', {'form': AddForm()})
```

### 简单的Form处理方法 + 表单验证

前端和后端最后都要做一次校验

```html
<h1>最原始的Form：全手工写+前端表单验证</h1>
<form action="." method="post">
    {% csrf_token %}
    <label>增加诗词信息: </label>
    author:<input id="author2" type="text" name="author" maxlength="10" minlength="1" value="{[ author ]}">
    title:<input id="title2" type="text" name="title" value="{[ title ]}">
    <input type="submit" value="OK">
</form>
```

```python
from django.shortcuts import render, HttpResponseRedirect
from .models import Poem


def add(request):
    if request.method == 'POST':
        author = request.POST.get('author', "")
        len_author = len(author)
        if len_author < 1 or len_author > 10:
            return render(request, 'add_poem.html')
        title = request.POST.get('title', "")

        poem = Poem(author=author, title=title)
        poem.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'add_poem.html')
```

## 自定义表单

### 简单实现自定义表单Froms.py

自定义一个表单【Froms.py】
```python
from django import forms


class AddForm(forms.Form):
    author = forms.CharField(label="the author", min_length=1, max_length=10)
    title = forms.CharField()
```

将表单导入视图函数输出到模板【views.py】
```
from django.shortcuts import render, HttpResponseRedirect
from .models import Poem
from .forms import AddForm


def add(request):
    #表单验证
    if request.method == 'POST':
        author = request.POST.get('author', "")
        len_author = len(author)
        if len_author < 1 or len_author > 10:
            return render(request, 'add_poem.html')
        title = request.POST.get('title', "")

        poem = Poem(author=author, title=title)
        poem.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'add_poem.html', {'form': AddForm()})
```

前端模板的使用
可以使用as_p或者as_label

```html
<h1>自定义From表单</h1>
<p>{{ errors }}</p>
<form action="." method="post">
    {% csrf_token %}
    <label>增加诗词信息: </label>
    {{ form.as_table }}
    <input type="submit" value="OK">
</form>
```

### 优化表单视图函数

通过自定义类来获取数据【views.py】
```python
from django.shortcuts import render, HttpResponseRedirect
from .models import Poem
from .forms import AddForm


# 使用自定义类来获取数据
    if request.method == 'POST':
        form = AddForm(request.POST)
        if not form.is_valid():
            print('invalid')
            return render(request, 'add_poem.html', {'form': AddForm()})
        author = form.cleaned_data['author']
        title = form.cleaned_data['title']
        poem = Poem(author=author, title=title)
        poem.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'add_poem.html', {'form': AddForm()})
```

### 通过Models来自定义表单

Models的定义【Models.py】
```python
from django.db import models

# Create your models here.
class Poem(models.Model):
    author = models.CharField(max_length=10)
    title = models.CharField(max_length=10)
```

自定义一个继承ModelForm表单【Froms.py】
```python
from django import forms
from .models import Poem


# 通过models来自定义表单
class AddForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['author', 'title']
```

### 自定义表单的验证

#### 通过Models.py来验证
Models的定义【Models.py】

```python
from django.db import models
from django.core.validators import ValidationError


# 先定义一个用于验证的函数
def validate_pre(value):
    print('author validate_pre')
    if not value.startswith('a'):
        raise ValidationError('u must start with a', code='invalid')
class Poem(models.Model):
    # 在对应的字段中引用
    author = models.CharField(max_length=10, validators=[validate_pre])
    title = models.CharField(max_length=10)
```

#### 通过Forms.py来验证


```
# ModelForm自定义表单 + 验证
class AddForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['author', 'title']
    
    # 仅用于测试，只能添加allen这个数据
    def clean_author(self):
        print('clean author')
        data = self.cleaned_data['author']
        if 'allen' not in data:
            raise ValidationError('not has allen')
        return data
```

```
# ModelForm自定义表单 + 验证
class AddForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['author', 'title']
    
    # 不允许数据重复
    def clean(self):
        print('clean')
        author = self.cleaned_data['author']
        title = self.cleaned_data['title']
        object = Poem.objects.filter(author=author, title=title)
        if object:
            raise ValidationError('dup')
```

#问题
这里有个顺序问题，哪个优先
