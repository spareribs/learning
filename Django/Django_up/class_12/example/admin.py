from django.contrib import admin, messages
from django import forms, template
from django.shortcuts import render
from .models import Poem, Article
from .forms import SetTypeForm


# Register your models here.

class SubInputText(forms.TextInput):
    class Media:
        css = {
            'all': ('input.css',)
        }


class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['author', 'title', 'type']
        widgets = {
            'author': forms.Textarea(attrs={'cols': '20', 'rows': '1'}),
            'title': SubInputText(),
            'type': forms.RadioSelect,
        }


class PoemModelAdmin(admin.ModelAdmin):
    form = PoemForm

    # self：当前发送的modeladmin
    # request：当前请求的页面
    # queryset：执行结果集
    def print_poem(self, request, queryset):
        for qs in queryset:
            print(qs)

    def set_type_action(self, request, queryset):
        if request.POST.get('post'):
            form = SetTypeForm(request.POST)
            if form.is_valid():
                type = form.cleaned_data['type']
            for qs in queryset:
                qs.type = type
                qs.save()
            # 设置友好的修改提示
            self.message_user(request, "{0}poems were changed with type:{1}".format(len(queryset), type))
            return None
        else:
            return render(request, 'set_type.html'
                          , {'form':
                                 SetTypeForm(
                                     initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
                              , 'objects': queryset})
    # 单个类型里面删除操作
    def get_actions(self, request):
        actions = super(PoemModelAdmin, self).get_actions(request)
        if 'hello' in actions:
            del actions['hello']
        return actions

    set_type_action.short_description = "修改诗词的类型"
    # 将print_poem和set_type_action注册到admin中
    actions = [print_poem, set_type_action]
    # 禁用actions
    # actions = None


def say_hello(modeladmin, req, queryset):
    print('hello')


admin.site.register(Poem, PoemModelAdmin)
admin.site.register(Article)
admin.site.add_action(say_hello, 'hello')
admin.site.disable_action('delete_selected')
