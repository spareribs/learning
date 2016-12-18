from django.shortcuts import render, HttpResponseRedirect
from .models import Poem
from .forms import AddForm


# Create your views here.
def home(request):
    return render(request, 'home.html', {'poems': Poem.objects.all()})


def add(request):
    # 最原始的方法
    # if request.method == 'POST':
    #     author = request.POST.get('author', "")
    #     title = request.POST.get('title', "")
    #     poem = Poem(author=author, title=title)
    #     poem.save()
    #     return HttpResponseRedirect('/')
    # else:
    #     return render(request, 'add_poem.html')

    # 表单验证
    # if request.method == 'POST':
    #     author = request.POST.get('author', "")
    #     len_author = len(author)
    #     if len_author < 1 or len_author > 10:
    #         return render(request, 'add_poem.html')
    #     title = request.POST.get('title', "")
    #
    #     poem = Poem(author=author, title=title)
    #     poem.save()
    #     return HttpResponseRedirect('/')
    # else:
    #     return render(request, 'add_poem.html')

    # 自定义表单
    # if request.method == 'POST':
    #     author = request.POST.get('author', "")
    #     len_author = len(author)
    #     if len_author < 1 or len_author > 10:
    #         return render(request, 'add_poem.html')
    #     title = request.POST.get('title', "")
    #
    #     poem = Poem(author=author, title=title)
    #     poem.save()
    #     return HttpResponseRedirect('/')
    # else:
    #     return render(request, 'add_poem.html', {'form': AddForm()})

    # 使用自定义类来获取数据
    if request.method == 'POST':
        form = AddForm(request.POST)
        if not form.is_valid():
            print('invalid')
            return render(request, 'add_poem.html', {'form': AddForm()})
        author = form.cleaned_data['author']
        title = form.cleaned_data['title']
        poem = Poem(author=author, title=title)
        poem.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'add_poem.html', {'form': AddForm()})
