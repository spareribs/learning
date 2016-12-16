from django import template
from datetime import datetime
from polls.models import Poem

# 模块必须包含一个模块级的变量:register,这是一个template.Library的实例,可以使用它来创建模板的过滤器和标签了.
register = template.Library()


# ----------------------------------------例子一
# # 这是template.Node的一个模板节点
# class AllenDateNode(template.Node):
#     def __init__(self, format_string):
#         self.format_string = format_string
#
#     def render(self, context):
#         # print(datetime.now().strftime(self.format_string))
#         # print(datetime.now().strftime("%Y-%m-%d %I:%M %p"))
#         # return datetime.now().strftime(self.format_string)
#         now = datetime.now().strftime(self.format_string)
#         context["mytime"] = now
#         return ""
#
# # parser 是模板分析器对象,在这个例子中我们没有使用它
# # token.contents 是包含有标签原始内容的字符串.在我们的例子中,它是'dateAllen "%Y-%m-%d %I:%M %p"'.
# @register.tag()
# def dateAllen(parse, token):
#     try:
#         # token.split_contents() 方法按空格拆分参数同时保证引号中的字符串在一起.
#         tagname, format_string = token.split_contents()
#         print(str(token.contents.split(' ')) + '--------------------')
#         print(token.split_contents())
#     except ValueError:
#         raise template.TemplateSyntaxError("invalid agrs")
#     # 这个函数返回一个 AllenDateNode,是Node子类,返回其它值都是错的
#     return AllenDateNode(format_string[1:-1])
#
# # 注册标签:模块 Library 实例注册这个标签.
# # register.tag(name="dateAllen", compile_function=dateAllen)


# ----------------------------------------例子二
# class AllenDateNode(template.Node):
#     def __init__(self, format_string, asvar):
#         self.format_string = format_string
#         self.asvar = asvar
#
#     def render(self, context):
#         now = datetime.now().strftime(self.format_string)
#         if self.asvar:
#             context[self.asvar] = now
#             return ""
#         else:
#             return now
#
#
# @register.tag()
# def dateAllen(parse, token):
#     args = token.split_contents()
#     asvar = None
#     if len(args) == 4 and args[-2] == "as":
#         asvar = args[-1]
#     elif len(args) != 2:
#         raise template.TemplateSyntaxError("invalid agrs")
#     return AllenDateNode(args[1][1:-1], asvar)

# ----------------------------------------例子三
# 进一步优化
@register.assignment_tag()
def get_current_time(format_string):
    return datetime.now().strftime(format_string)

# 将
@register.inclusion_tag("resultes.html")
def pomes_of_author(author_name):
    poems = Poem.objects.filter(author=author_name)
    return {"pomes": poems, "author_name": author_name}
