from django.contrib import admin
from django import forms
from .models import Poem


# Register your models here.

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
            # 修改为Textarea的Forms，在设置对应的属性
            'author': forms.Textarea(attrs={'cols': '20', 'rows': '1'}),
            # 设置背景样式
            'title': SubInputText(),
            # 修改成RadioSelect的选择框
            'type': forms.RadioSelect,
        }


class PoemModelAdmin(admin.ModelAdmin):
    form = PoemForm


admin.site.register(Poem, PoemModelAdmin)
