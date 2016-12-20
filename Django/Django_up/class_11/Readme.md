# 知识点

1. 修改字段默认widget
2. 设置widget属性
3. 自定义widget

# 简介

## 参考文档
[代码地址：Spareibs的Github](https://github.com/spareribs/learning/tree/master/Django/Django_up/class_11)

# 实验步骤
直接修改修改Form中的内容【admin.py】
```
class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['author', 'title', 'type']
        widgets = {
            'author': forms.Textarea(attrs={'cols': '20', 'rows': '1'}),
            'title': SubInputText(),
            'type': forms.RadioSelect,
        }
```

## TextInput类样式的修改
```
# 设置背景样式的子类
class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['author', 'title', 'type']
        widgets = {
            # 修改为Textarea的Forms，在设置对应的属性
            'author': forms.Textarea(attrs={'cols': '20', 'rows': '1'}),
        }
```
## 自定义TextInput的子类SubInputText

自定义的css格式文件
```css
input[type=text]{
    background-color: aquamarine;
}
```


```python
# 设置背景样式的子类
class SubInputText(forms.TextInput):
    class Media:
        css = {
            'all': ('input.css',)
        }

class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['author', 'title', 'type']
        widgets = {
            # 设置背景样式
            'title': SubInputText(),
        }
```
## 修改成RadioSelect的选择框
```
class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['author', 'title', 'type']
        widgets = {
            # 修改成RadioSelect的选择框
            'type': forms.RadioSelect,
        }
```