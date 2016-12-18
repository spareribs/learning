from django.db import models
from django.core.validators import ValidationError

# Create your models here.

# 先定义一个用于验证的函数
def validate_pre(value):
    print('author validate_pre')
    if not value.startswith('a'):
        raise ValidationError('u must start with a', code='invalid')
class Poem(models.Model):
    # 在对应的字段中引用
    author = models.CharField(max_length=10, validators=[validate_pre])
    title = models.CharField(max_length=10)
