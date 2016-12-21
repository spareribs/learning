from django.dispatch import Signal, receiver
from django.db.models.signals import pre_save, post_save
from .models import Poem, Task

signalAllen = Signal(providing_args=['allen'])


@receiver(signalAllen)
def signal_callback(sender, **kwargs):
    print(sender, kwargs)
    print('signal_callback called')

# 注册，或者使用装饰器注册
# signalAllen.connect(signal_callback)

# 可以定义多个
@receiver(signalAllen)
def signal_callback1(sender, **kwargs):
    print(sender, kwargs)
    print('signal_callback1 called')


@receiver(pre_save)
def pre_save_callback(sender, **kwargs):
    print('pre_save_callback')


@receiver(post_save)
def post_save_callback(sender, **kwargs):
    print('post_save_callback')