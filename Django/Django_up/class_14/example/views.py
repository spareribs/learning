from django.http import Http404, HttpResponse
from .models import Poem


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


import ast


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
