from django.conf.urls import url
from .views import index, IndexView, ShowTasksView, DisplaySingleTaskView, AddModelView
from django.views.generic import TemplateView, RedirectView
from .forms import AddPoemForm

urlpatterns = [
    # 在view中指定访问主页的类
    url(r'^index/$', IndexView.as_view()),
    # 直接指定需要访问的主页，不需要添加导入和编写views的逻辑
    # url(r'^index/$', IndexView.as_view(template_name='tasks.html')),
    # RedirectView跳转到百度的页面
    url(r'^redirect/$', RedirectView.as_view(url='http://baidu.com')),
    # ListView:显示对象的列表
    url(r'^tasks/$', ShowTasksView.as_view()),
    # 通过task_id仅显示一个task
    url(r'^task/(?P<task_id>\d+)/$', DisplaySingleTaskView.as_view()),
    # 添加task的url
    url(r'^addtask/$', AddModelView.as_view()),
    # 添加poem的url
    url(r'^addpoem/$', AddModelView.as_view(form_class=AddPoemForm)),
    # 添加task成功的url
    url(r'^success/$', TemplateView.as_view(template_name='post_success.html')),
]
