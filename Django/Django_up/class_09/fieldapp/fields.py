from django.db import models
import ast

# 自定义一个ListFiled,继承与TextField这个类
class ListFiled(models.TextField):
    description = "just a listfiled"

    # 继承TextField
    def __init__(self, *args, **kwargs):
        super(ListFiled, self).__init__(*args, **kwargs)
    # 读取数据库的时候调用这个方法
    def from_db_value(self, value, expression, conn, context):
        print('from_db_value')
        if not value:
            value = []
        if isinstance(value, list):
            return value
        print('value type ', type(value))
        # 直接将字符串转换成python内置的list
        return ast.literal_eval(value)

    # 保存数据库的时候调用这个方法
    def get_prep_value(self, value):
        print("get_prep_value")
        if not value:
            return value
        print('value type ', type(value))
        return str(value)

from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

class ContextTypeRestrictedFileField(FileField):
    def __init__(self, content_type=None, max_upload_size=None, **kwargs):
        self.content_type = content_type
        self.max_upload_size = max_upload_size
        super(ContextTypeRestrictedFileField, self).__init__(**kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContextTypeRestrictedFileField, self).clean(*args, **kwargs)
        file = data.file
        try:
            type = file.content_type
            if type != self.content_type:
                raise forms.ValidationError('pls upload right filetype')
            if file.size > self.max_upload_size:
                raise forms.ValidationError('exceed max uploadsize')
        except AttributeError:
            print("error")
            pass
        return data