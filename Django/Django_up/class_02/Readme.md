# 知识点

1. 可以通过过滤器来修改变量的显示，过滤器的形式是：{{ variable | filter }}，管道符号'|'代表使用过滤器 
2. 过滤器能够采用链式的方式使用，例如：{{ text | escape | linebreaks }} 
3. 过滤器还可以带参数，例如： {{ bio|truncatewords:30 }} 
4. 过滤器的参数中如果带有空格，那么需要用引号引起来，例如：{{ list | join : ", "}} 
5. django中有30多个内置过滤器 比如add，cut，date等。 

# 参考文档

# 实验步骤

结合class_01的内容继续往下

## 在templatetags的文件夹下面创建过滤器poll_filter.py

### 例子一：去掉字符串中的空格

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django进阶课程</title>
</head>
<body>
<p>欢迎来到Django进阶课程</p>
{% load poll_filter %}
{{ "all en" | cut_filter:" " }}
</body>
</html>
```

```python
from django import template

register = template.Library()

def cut_filter(value, arg):
    return value.replace(arg, '')

register.filter(name="cut_filter", filter_func=cut_filter)
```

或者使用装饰器来注册

```python
from django import template

register = template.Library()

@register.filter()
def cut_filter(value, arg):
    return value.replace(arg, '')
```

### 例子二：将字母变成小写
```python
from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter()
@stringfilter
def lower(value):
    return value.lower()
```


# 例子三：Django自定义过滤器是否会自动转义

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django进阶课程</title>
</head>
<body>
<p>欢迎来到Django进阶课程</p>
{% load poll_filter %}
{% with "<h1>hello</h1>" as tmpValue %}
    <p>{{ tmpValue | capfirst }}</p>
    <hr>
    <p>{{ tmpValue | add_no:"world" }}</p>
    <hr>
    <p>{{ tmpValue | add_yes:"world" }}</p>
{% endwith %}

</body>
</html>
```

```python
from django import template
from django.utils.safestring import mark_safe
register = template.Library()

# 没有自动转义
@register.filter()
def add_no(value, arg):
    return "%s %s" %(value, arg)

# 有自动转义：is_safe 或者mark_safe
@register.filter(is_safe=True)
def add_yes(value, arg):
    return mark_safe("%s %s" %(value, arg))
```
