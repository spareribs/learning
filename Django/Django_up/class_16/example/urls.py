from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.index),
    url(r'^disconnect/$', view=views.disconnect_signal),
    url(r'^modify/$', view=views.modify),
]