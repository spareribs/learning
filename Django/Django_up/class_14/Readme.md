# 知识点

1. 使用Json场景
2. Json基本介绍
3. 在Django Model中使用Json

# 简介

# 使用场景
1. 我们在开发网站的时候，有时候只需要更新数据给前端，而不是刷新整个页面，比如讲我们的model里的全部或者部分数据返回给前端，这个时候，前端为了效率，往往使用ajax，后端django发送数据的时候往往采用json协议，也就是发送json串给前端。同时，前端也可以传递json数据到web后端。
2. Models -> JSON

# Json基本介绍
JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。 易于人阅读和编写。同时也易于机器解析和生成。

# JSON格式
```js
{
    "result_count": 3, 
    "results": [
        {
            "_href": "/ws.v1/lswitch/3ca2d5ef-6a0f-4392-9ec1-a6645234bc55", 
            "type": "LogicalSwitchConfig"
        }, 
        {
            "_href": "/ws.v1/lswitch/81f51868-2142-48a8-93ff-ef612249e025", 
            "type": "LogicalSwitchConfig"
        }, 
    ]
}

```
## 参考文档
[代码地址：Spareibs的Github](https://github.com/spareribs/learning/tree/master/Django/Django_up/class_14)

# 实验操作

## JSON获取数据的方法

前段html文件
```
<div class="container">
    <div class="container">
        <h3>Poems:</h3>
        <ul>
            <li>Results:</li>
        </ul>
        <button class="btn get-more">Get More Poems</button>
    </div>
</div>
```


```
$('.get-more').click(function () {
    $.ajax({
        // 通过get请求获取更多的pome信息
        type: "GET",
        url: "/ajax/more",
        dataType: 'json',
        success: function (data) {
            // 先将内容转换成字符串
            json_str = JSON.stringify(data)
            // 再将字符串格式化
            json_data = JSON.parse(json_str)
            // 遍历json_data
            for (var i in json_data) {
                item = json_data[i];
                $('ul').append('<li>' + item.poem_id + " " + item.author + '</li>')
            }
        }
    })
});
```

【views.py】
```
from django.http import Http404, HttpResponse


def more_poems(request):
    if request.is_ajax():
        objects = Poem.objects.all()
        # [{author:'allen',title:'1'},{}]
        data = get_json_objects(objects, Poem)
        print(str(data) + "这是data  more_poems77777777777777777777")
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404


def json_filed(field_data):
    if isinstance(field_data, str):
        return "\"" + field_data + "\""
    if isinstance(field_data, bool):
        if field_data == 'False':
            return 'false'
        else:
            return 'true'
    return str(field_data)


def json_encode_dict(dict_data):
    print(str(dict_data) + "这是dict_data  json_encode_dict333333333333333")
    json_data = "{"
    for (k, v) in dict_data.items():
        json_data = json_data + json_filed(k) + ": " + json_filed(v) + ", "
    json_data = json_data[:-2] + "}"
    print(str(json_data) + "这是json_data json_encode_dict44444444444444444")
    return json_data


def json_encode_list(list_data):
    print(str(list_data) + "这是list_fata  json_encode_list2222222222222222222")
    json_res = "["
    for item in list_data:
        json_res = json_res + json_encode_dict(item) + ", "
    print(str(json_res[:-2]) + "]" + "这是json_res json_encode_list555555555555555555555")
    return json_res[:-2] + "]"


def get_json_objects(objects, model_meta):
    print(str(objects) + "这是objects get_json_objects111111111111111111111111")
    concrete_model = Poem._meta.concrete_model
    list_data = []
    for obj in objects:
        dict_data = {}
        for field in concrete_model._meta.local_fields:
            if field.name == 'id':
                continue
            value = field.value_from_object(obj)
            dict_data[field.name] = value

        list_data.append(dict_data)

    data = json_encode_list(list_data)
    print(str(data) + "这是data get_json_objects66666666666666666666666")
    return data
```

【urls.py】
```
urlpatterns = [
    url(r'ajax/more/$', view=views.more_poems),
]
```

数据的处理过程如下
```cmd
[<Poem: 静夜思>, <Poem: 早发白帝城>, <Poem: 陌上桑>, <Poem: 锄禾日当午>]这是objects get_json_objects111111111111111111111111
[{'poem_id': 0, 'author': '李白', 'title': '静夜思'}, {'poem_id': 1, 'author': '王维', 'title': '早发白帝城'}, {'poem_id': 3, 'author': '李白', 'title': '陌上桑'}, {'poem_id': 4, 'author': '王维', 'title': '锄禾日当午'}]这是list_fata  json_encode_list2222222222222222222
{'poem_id': 0, 'author': '李白', 'title': '静夜思'}这是dict_data  json_encode_dict333333333333333
{"poem_id": 0, "author": "李白", "title": "静夜思"}这是json_data json_encode_dict44444444444444444
{'poem_id': 1, 'author': '王维', 'title': '早发白帝城'}这是dict_data  json_encode_dict333333333333333
{"poem_id": 1, "author": "王维", "title": "早发白帝城"}这是json_data json_encode_dict44444444444444444
{'poem_id': 3, 'author': '李白', 'title': '陌上桑'}这是dict_data  json_encode_dict333333333333333
{"poem_id": 3, "author": "李白", "title": "陌上桑"}这是json_data json_encode_dict44444444444444444
{'poem_id': 4, 'author': '王维', 'title': '锄禾日当午'}这是dict_data  json_encode_dict333333333333333
{"poem_id": 4, "author": "王维", "title": "锄禾日当午"}这是json_data json_encode_dict44444444444444444
[{"poem_id": 0, "author": "李白", "title": "静夜思"}, {"poem_id": 1, "author": "王维", "title": "早发白帝城"}, {"poem_id": 3, "author": "李白", "title": "陌上桑"}, {"poem_id": 4, "author": "王维", "title": "锄禾日当午"}]这是json_res json_encode_list555555555555555555555
[{"poem_id": 0, "author": "李白", "title": "静夜思"}, {"poem_id": 1, "author": "王维", "title": "早发白帝城"}, {"poem_id": 3, "author": "李白", "title": "陌上桑"}, {"poem_id": 4, "author": "王维", "title": "锄禾日当午"}]这是data get_json_objects66666666666666666666666
[{"poem_id": 0, "author": "李白", "title": "静夜思"}, {"poem_id": 1, "author": "王维", "title": "早发白帝城"}, {"poem_id": 3, "author": "李白", "title": "陌上桑"}, {"poem_id": 4, "author": "王维", "title": "锄禾日当午"}]这是data  more_poems77777777777777777777
```


## JSON提交数据的方法

前段html文件
```html
<div class="container">
    <label>Poems</label>
    <textarea class="textArea" id="textArea" rows="10" cols="70"> </textarea>
    <button class="btn add-poem">Add Poem</button>
</div>
```


【views.py】
```
from django.http import Http404, HttpResponse


def add(request):
    if request.is_ajax() and request.POST:
        json_str = request.POST.get('poems')
        data = "post success"
        json_list = ast.literal_eval(json_str)
        for item in json_list:
            new_obj = Poem()
            for filed in item:
                setattr(new_obj, filed, item[filed])
            print(new_obj.author, new_obj.title, new_obj.poem_id)
            new_obj.save()
        return HttpResponse(data, content_type='application/text')
    else:
        return Http404
```


```
$('.add-poem').click(function () {
    $.ajax({
        type: "POST",
        url: "/ajax/add/",
        dataType: 'text',
        data: {"poems": $(".textArea").val()},
        success: function (data) {
            alert(data);
        }
    });

});
```

【urls.py】
```
urlpatterns = [
    url(r'ajax/add/$', view=views.add),
]
```

提交数据的格式
```cmd
[{"poem_id": 10, "author": "排骨", "title": "Django"}]
```

