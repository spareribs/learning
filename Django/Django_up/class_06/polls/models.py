# -*- coding: utf-8 -*-
from mongoengine import *


# Create your models here.
class Poem(Document):
    # poem
    meta = {
        # 数据库中显示的名字
        'collection': 'poem_data'
    }
    poem_id = SequenceField(required=True, primary_key=True)
    author = StringField()
    title = StringField()

    # 可以定义查询集
    @queryset_manager
    def show_newest(doc_cls, queryset):
        # 通过poem_id降序显示
        return queryset.order_by('-poem_id')
