# 知识点

1. 如何定义普通操作
2. 如何定义中间页面
3. 整个站点应用操作
4. 不同ModelAdmin应用操作


# 简介

## 参考文档
[代码地址：Spareibs的Github](https://github.com/spareribs/learning/tree/master/Django/Django_up/class_12)

# 实验操作

## admin.ModelAdmin的子类PoemModelAdmin设置操作【admin.py】
```
class PoemModelAdmin(admin.ModelAdmin):
    form = PoemForm
    # self：当前发送的modeladmin
    # request：当前请求的页面
    # queryset：执行结果集
    def print_poem(self, request, queryset):
        for qs in queryset:
            print(qs)

    def set_type_action(self, request, queryset):
        for qs in queryset:
            qs.type = 2
            qs.save()
        # 设置友好的修改提示
        self.message_user(request, "{0}poems were changed with type:{1}".format(len(queryset), 2))

    set_type_action.short_description = "修改诗词的类型[唐诗-->宋词]"
    # 将print_poem和set_type_action注册到admin中
    actions = [print_poem, set_type_action]
    
```

## 确认操作页面

先定义一个from
```python
from django import forms

class SetTypeForm(forms.Form):
    type = forms.IntegerField()
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
```

定义一个模板【set_type.html】
```html
{% extends "admin/base_site.html" %}

{% load i18n admin_urls %}

{% block content %}
    <form action="" method="post"> {% csrf_token %}
    {{ form.as_p }}
    <ul>
        {% for ob in objects %}
            <li>{{ ob }}</li>
        {% endfor %}
    </ul>
    <!--value是admin的内容-->
    <input type="hidden" name="action" value="set_type_action">
    <input type="hidden" name="post" value="yes">
    <input type="submit" name="apply" value="set">
    </form>
{% endblock %}
```

实现中间页面的操作【admin.py】
```python
class PoemModelAdmin(admin.ModelAdmin):
    form = PoemForm

    # self：当前发送的modeladmin
    # request：当前请求的页面
    # queryset：执行结果集
    def print_poem(self, request, queryset):
        for qs in queryset:
            print(qs)

    def set_type_action(self, request, queryset):
        if request.POST.get('post'):
            form = SetTypeForm(request.POST)
            if form.is_valid():
                type = form.cleaned_data['type']
            for qs in queryset:
                qs.type = type
                qs.save()
            # 设置友好的修改提示
            self.message_user(request, "{0}poems were changed with type:{1}".format(len(queryset), type))
            return None
        else:
            return render(request, 'set_type.html'
                          , {'form':
                                 SetTypeForm(
                                     initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
                              , 'objects': queryset})

    set_type_action.short_description = "修改诗词的类型"
    # 将print_poem和set_type_action注册到admin中
    actions = [print_poem, set_type_action]
```

## 设置Modeadmin全局的操作action【admin.py】

添加全局操作
```python
def say_hello(modeladmin, req, queryset):
    print('hello')

admin.site.add_action(say_hello, 'hello')
```

删除全局操作
```python
admin.site.disable_action('delete_selected')

```

## 单个Modeadmin删除操作action【admin.py】
```python
# 单个类型里面删除操作
    def get_actions(self, request):
        actions = super(PoemModelAdmin, self).get_actions(request)
        if 'hello' in actions:
            del actions['hello']
        return actions
```

## 单个单个Modeadmin禁用action【admin.py】
```
# 禁用actions
actions = None
```