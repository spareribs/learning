# 知识点

1. Jinja2介绍
2. 如何用Jinja2替换Django自带模版
3. 在Django中简单使用Jinja2


# 参考文档
[代码地址：Spareibs的Github](https://github.com/spareribs/learning/tree/master/Django/Django_up/class_03)

# Jinja2介绍

> Jinja2 是一个现代的，设计者友好的，仿照 Django 模板的 Python 模板语言。 它速度快，被广泛使用，并且提供了可选的沙箱模板执行环境保证安全。


# 实验步骤

## 安装Jinja2的库

```python
(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_03>pip install jinja2
Collecting jinja2
  Using cached Jinja2-2.8-py2.py3-none-any.whl
Collecting MarkupSafe (from jinja2)
  Using cached MarkupSafe-0.23.tar.gz
Building wheels for collected packages: MarkupSafe
  Running setup.py bdist_wheel for MarkupSafe ... done
  Stored in directory: C:\Users\Administrator\AppData\Local\pip\Cache\wheels\a3\fa\dc\0198eed9ad95489b8a4f45d14dd5d2aee3f8984e46862c5748
Successfully built MarkupSafe
Installing collected packages: MarkupSafe, jinja2
Successfully installed MarkupSafe-0.23 jinja2-2.8
```

## 在项目文件目录下面新建一个模板引擎jinja2.py
```python
from jinja2 import Environment

def environment(**options):
    env = Environment(**options)
    return env
```

## 设置settings.py文件
```
TEMPLATES = [
    {
        # 替换backends
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'polls/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'my_blog.jinja2.environment',

        },
    },
]
```

## 使用jinja例子

### 例子一：jinja常见的语法
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django进阶课程</title>
</head>
<body>
<p>欢迎来到Django进阶课程</p>
<div>
    {% for i in tmpValue %}
        {{ i }}
    {% endfor %}
</div>
<hr>
<div>
    {% for i in tmpValue %}
        {% if i ==1 %}
            {{ i }}
        {% endif %}
    {% endfor %}
</div>
<hr>
<div>
    {{ 1 + 2 }}
    {{ 1 / 2 }}
    {{ 10 % 3 }}
    {{ 2 ** 3 }}
    <hr>
    {% set tmpInt = 10 %}
    {{ tmpInt }}
    <hr>
    {{ -1 | abs }}
    {{"abc" | capitalize }}
</div>
</body>
</html>
```

### 例子二：自定义过滤器

poll_filter.py

```python
def cut_filter(value, arg):
    return value.replace(arg, '')

def lower(value):
    return value.lower()
```

```python
from jinja2 import Environment
from polls.templatetags.poll_filter import lower

def environment(**options):
    env = Environment(**options)
    env.filters['allen_lower'] = lower
    return env
```

jinja2.py

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django进阶课程</title>
</head>
<body>
<p>欢迎来到Django进阶课程</p>
<div>
    {{"abc" | capitalize | allen_lower }}
</div>
</body>
</html>
```

## 问题
如何将jinja2和Django混合使用