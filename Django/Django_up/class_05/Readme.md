# 知识点

1. 以Mysql的数据库为例，集成已有的数据库

# 参考文档
[第十八章： 集成已有的数据库和应用](http://djangobook.py3k.cn/2.0/chapter18/)
[代码地址：Spareibs的Github](https://github.com/spareribs/learning/tree/master/Django/Django_up/class_05)

# 实验步骤

##class_04数据库中的设置

查看项目的配置文件【settings.py】
这里先执行inspectdb，然后再修改
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

## 修改Database的配置

注意需要手动创建django_advanced的数据库
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_advanced',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}



```

## 修改默认的mysql驱动引擎【__init__.py】

```python
import pymysql
pymysql.install_as_MySQLdb()
```

## 可以查看帮助文档【manage.py】

```python
(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_05>python manage.py --help

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    inspectdb

(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_05>python manage.py inspectdb --help
usage: manage.py inspectdb [-h] [--version] [-v {0,1,2,3}]
                           [--settings SETTINGS] [--pythonpath PYTHONPATH]
                           [--traceback] [--no-color] [--database DATABASE]

Introspects the database tables in the given database and outputs a Django
model module.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v {0,1,2,3}, --verbosity {0,1,2,3}
                        Verbosity level; 0=minimal output, 1=normal output,
                        2=verbose output, 3=very verbose output
  --settings SETTINGS   The Python path to a settings module, e.g.
                        "myproject.settings.main". If this isn't provided, the
                        DJANGO_SETTINGS_MODULE environment variable will be
                        used.
  --pythonpath PYTHONPATH
                        A directory to add to the Python path, e.g.
                        "/home/djangoprojects/myproject".
  --traceback           Raise on CommandError exceptions
  --no-color            Don't colorize the command output.
  --database DATABASE   Nominates a database to introspect. Defaults to using
                        the "default" database.
```

## 先在sqlite3的数据库中导出数据表的结构【settings.py】
```
(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_05>python manage.py inspectdb >> polls/models.py
```

## 然后切换成mysql的数据库同步数据库【settings.py】

makemigrations > migrate > createsuperuser > runserver
```
(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_05>python manage.py makemigrations
Migrations for 'polls':
  0007_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django.py:
    - Create model AuthGroup
    - Create model AuthGroupPermissions
    - Create model AuthPermission
    - Create model AuthUser
    - Create model AuthUserGroups
    - Create model AuthUserUserPermissions
    - Create model DjangoAdminLog
    - Create model DjangoContentType
    - Create model DjangoMigrations
    - Create model DjangoSession
    - Create model PollsPoem
    - Create model PollsTodo

(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_05>python manage.py migrate
Operations to perform:
  Apply all migrations: sessions, admin, polls, auth, contenttypes
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying polls.0001_initial... OK
  Applying polls.0002_auto_20160507_0634... OK
  Applying polls.0003_auto_20160507_0654... OK
  Applying polls.0004_auto_20160507_0700... OK
  Applying polls.0005_auto_20160507_0705... OK
  Applying polls.0006_todo... OK
  Applying polls.0007_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django... OK
  Applying sessions.0001_initial... OK

(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_05>python manage.py createsuperuser
Username (leave blank to use 'spareribs'): admin
Email address: 370835062@qq.com
Password:
Password (again):
Superuser created successfully.

(env_py35_django) D:\MaiZi_Edu\Dropbox\Maizi\Django_up\class_05>python manage.py runserver
```

## 问题
数据没有过来怎么解决？我是通过数据库的命令将数据导过去的
inspectdb就像是之保存了数据库的结构--->如果不行，只能自己想方法了