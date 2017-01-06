# coding: utf-8
# author: spareribs


from django.contrib import admin
from models import *


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # admin 选项控制变更列表所显示的列
    list_display = ('title', 'desc', 'click_count',)
    # admin 选项控制变更列表可以链接的列
    list_display_links = ('title', 'desc',)
    # admin 选项控制变更列表可以直接编辑的列
    list_editable = ('click_count',)

    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content')
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend', 'user', 'category', 'tag')
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


admin.site.register(User)
admin.site.register(Tag)
# 默认Django的ModelAdmin来注册
# admin.site.register(Article)
# 使用自定义的ModelAdmin来注册
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
