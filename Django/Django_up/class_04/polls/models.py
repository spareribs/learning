# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Poem(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s" %(self.author, self.title)

# IncompleteTodoManager是继承Manager的一个子类，返回未完成的事件的结果集
class IncompleteTodoManager(models.Manager):
    # 重载get_queryset的方法
    def get_queryset(self):
        return super(IncompleteTodoManager, self).get_queryset().filter(is_done=False)

# HighPriorityManager是指定优先级的结果集
class HighPriorityManager(models.Manager):
    def get_queryset(self):
        return super(HighPriorityManager, self).get_queryset().filter(priority=1)

class ToDoManager(models.Manager):
    def incomplete(self):
        return self.filter(is_done=False)

    def high(self):
        return self.filter(priority=1)

class TodoQuerySet(models.QuerySet):
    def incomplete(self):
        return self.filter(is_done=False)

    def high(self):
        return self.filter(priority=1)

class NewTodoManager(models.Manager):
    def get_queryset(self):
        return TodoQuerySet(self.model, using=self._db)

    def incomplete(self):
        return self.get_queryset().incomplete()

    def high(self):
        return self.get_queryset().high()

class ToDo(models.Model):
    content = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return "%s-%d" %(self.content,self.priority)

    # 实例化
    objects = NewTodoManager()
    #
    # objects = ToDoManager()
    # 这燕子修改以后，views就不能用默认的objects来调用
    todolists = models.Manager()
    # 实例化一个IncompleteTodoManager，结果集是未完成的事件数据
    incomplete = IncompleteTodoManager()
    high = HighPriorityManager()
