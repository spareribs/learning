from django.contrib import admin
from .models import Poem
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class MyUserAdmin(UserAdmin):
    # 显示在管理页面的字段
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    # 定制过滤器
    list_filter = ('is_staff',)
    # 可查询字段
    search_fields = ('last_name',)

# 需要将User取消注册，然后再注册到MyUserAdmin里面
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)


class PoemModelAdmin(admin.ModelAdmin):
    # 显示在管理页面的字段
    list_display = ['title', 'timestamp', 'author']
    # 可以修改内容的链接
    list_display_links = ['author']
    # 可以查询的字段，显示搜索框
    search_fields = ['title']
    # 可直接编辑的字段（但是不能同时可连接可编发来）
    list_editable = ['title']
    # 定制过滤器
    list_filter = ['author']

    # 自定义模板
    change_form_template = 'change_form.html'

    class Meta:
        model = Poem
admin.site.register(Poem, PoemModelAdmin)
