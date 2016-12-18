# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Poem(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s" % (self.author, self.title)


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
        return "%s-%d" % (self.content, self.priority)

    # 实例化
    objects = NewTodoManager()
    #
    # objects = ToDoManager()
    # 这燕子修改以后，views就不能用默认的objects来调用
    todolists = models.Manager()
    # 实例化一个IncompleteTodoManager，结果集是未完成的事件数据
    incomplete = IncompleteTodoManager()
    high = HighPriorityManager()


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PollsPoem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'polls_poem'


class PollsTodo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content = models.CharField(max_length=200)
    is_done = models.BooleanField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'polls_todo'

class Book2(models.Model):
    author = models.CharField(max_length=1024, blank=True, null=True)
    title = models.CharField(max_length=1024)

    class Meta:
        app_label = 'polls2'