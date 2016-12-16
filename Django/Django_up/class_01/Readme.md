# 知识点

- 模版是一个用django模版语言标记过的python字符串。模版可以包含模版标签和变量。
- 模版标签是在一个模版里起作用的标记。比如，一个模版标签可以产生控制结构的内容(if或者for)，可以获取数据库内容或者访问其它模版标签。
- 一个标签块被{%%}包围
- 变量标签被{{}}包围
- context是一个传递给模版的key-value对。
- 模版渲染是通过从context获取值来替换模版中变量并执行所有的模版标签。

# 参考文档
[第十章: 深入模板引擎](http://djangobook.py3k.cn/chapter10/)
代码地址： [Spareibs的Github](https://github.com/spareribs/learning/Django/Django_up/class_01/)

# 实验步骤
## 新创建一个templatetags的文件夹

```
|---templatetags
    |---poll_extras.py
```

## 创建超级用户并启动程序

```
(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_01>python manage.py createsuperuser
D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_01\my_blog\urls.py:22: RemovedInDjango110Warning: Support for string view arguments to url() is deprecated and will be removed in Django 1.10 (got polls.views.home). Pass the callable instead.
  url(r'^$', 'polls.views.home'),

Username (leave blank to use 'spareribs'): admin
Email address: 370835062@qq.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
Password:
Password (again):
Superuser created successfully.

(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_01>python manage.py runserver
```
这里的管理员
账号：admin
密码是：adminadmin

## 实验例子：根据指定的日期格式来显示日期的自定义标签

### 方法一
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django进阶课程</title>
</head>
<body>
<p>欢迎来到Django进阶课程</p>
{% load poll_extras%}
{% dateAllen "%Y-%m-%d %I:%M %p"%}
<p>It is {{ mytime }} </p>
</body>
</html>
```

```python
# 模块必须包含一个模块级的变量:register,这是一个template.Library的实例,可以使用它来创建模板的过滤器和标签了.
register = template.Library()

# 这是template.Node的一个模板节点
class AllenDateNode(template.Node):
    def __init__(self, format_string):
        self.format_string = format_string

    def render(self, context):
        print(datetime.now().strftime(self.format_string))
        print(datetime.now().strftime("%Y-%m-%d %I:%M %p"))
        return datetime.now().strftime(self.format_string)

# parser 是模板分析器对象,在这个例子中我们没有使用它
# token.contents 是包含有标签原始内容的字符串.在我们的例子中,它是'dateAllen "%Y-%m-%d %I:%M %p"'.
def dateAllen(parse, token):
    try:
        # token.split_contents() 方法按空格拆分参数同时保证引号中的字符串在一起.
        tagname, format_string = token.split_contents()
        print(str(token.contents.split(' ')) + '--------------------')
        print(token.split_contents())
    except ValueError:
        raise template.TemplateSyntaxError("invalid agrs")
    # 这个函数返回一个 AllenDateNode,是Node子类,返回其它值都是错的
    return AllenDateNode(format_string[1:-1])

# 注册标签:模块 Library 实例注册这个标签.
register.tag(name="dateAllen", compile_function=dateAllen)
```

- 可以使用装饰器优化注册的方法

```python
@register.tag()
def dateAllen(parse, token):
    try:
        # token.split_contents() 方法按空格拆分参数同时保证引号中的字符串在一起.
        tagname, format_string = token.split_contents()
        print(str(token.contents.split(' ')) + '--------------------')
        print(token.split_contents())
    except ValueError:
        raise template.TemplateSyntaxError("invalid agrs")
    # 这个函数返回一个 AllenDateNode,是Node子类,返回其它值都是错的
    return AllenDateNode(format_string[1:-1])
```


### 方法二

- 做成全局的模板变量,方便其他地方引用
```python
def render(self, context):
    now = datetime.now().strftime(self.format_string)
    context["mytime"] = now
    return ""
```
但是这样子会把代码写死成mytime的硬编码

- 优化硬编码问题
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django进阶课程</title>
</head>
<body>
<p>欢迎来到Django进阶课程</p>
{% load poll_extras%}
{% dateAllen "%Y-%m-%d %I:%M %p" as allentime %}
<p>It is {{ allentime }} </p>
</body>
</html>
```

```python
class AllenDateNode(template.Node):
    def __init__(self, format_string, asvar):
        self.format_string = format_string
        self.asvar = asvar

    def render(self, context):
        now = datetime.now().strftime(self.format_string)
        if self.asvar:
            context[self.asvar] = now
            return ""
        else:
            return now


@register.tag()
def dateAllen(parse, token):
    args = token.split_contents()
    asvar = None
    if len(args) == 4 and args[-2] == "as":
        asvar = args[-1]
    elif len(args) != 2:
        raise template.TemplateSyntaxError("invalid agrs")
    return AllenDateNode(args[1][1:-1], asvar)
```

### 例子三：:assignment_tag

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django进阶课程</title>
</head>
<body>
<p>欢迎来到Django进阶课程</p>
{% load poll_extras %}
{% get_current_time "%Y-%m-%d %I:%M %p" as allentime %}
<p>It is {{ allentime }} </p>

</body>
</html>
```

```python
@register.assignment_tag()
def get_current_time(format_string):
    return datetime.now().strftime(format_string)
```

### 例子四:inclusion_tag

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django进阶课程</title>
</head>
<body>
<p>欢迎来到Django进阶课程</p>
{% pomes_of_author "李白" %}
</body>
</html>
```

```python
@register.assignment_tag()
def get_current_time(format_string):
    return datetime.now().strftime(format_string)
```

```python
# 从模板中导入
from polls.models import Poem

# 
@register.inclusion_tag("resultes.html")
def pomes_of_author(author_name):
    poems = Poem.objects.filter(author=author_name)
    return {"pomes": poems, "author_name": author_name}
```