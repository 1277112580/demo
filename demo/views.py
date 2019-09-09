from django.http import HttpResponse
from django.template import Template,Context

def index(request):
    '''
    视图
    :param request: 
    :return: 
    '''
    return HttpResponse('hello，world')
def about(request):
    return HttpResponse('about页面')

def gethtml(request):
    html="""
    <html>
        <head>
        </head>
        <body>
        <h1>这是一级标签</h1>
        <h2>{{name}}</h2>
        <img src='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1568004495062&di=f22c60f760eca250080a4fbbfdd49093&imgtype=0&src=http%3A%2F%2Fimage.finance.china.cn%2Fupload%2Fimages%2F2014%2F0410%2F085000%2F0_2323627_580fd395d60d023a4cf8b45c31cd1218.jpg'>
        <p>{{content}}</p>
        </body>
    </html>
    """
    # 1.构建模板结构
    tempalte_obj=Template(html)
    # 2.创建渲染模板
    params=dict(name='风景',content='山')
    content_obj=Context(params)
    # 3.进行数据渲染
    result=tempalte_obj.render(content_obj)
    # 4.返回结果
    # return HttpResponse(html)
    return HttpResponse(result)

from django.shortcuts import  render
def indextmp(request):
    name='哈士奇111'
    return render(request,'index.html',{'name':name})

# from django.shortcuts import render_to_response
# def abc(request):
#     name='hello'
#     return render_to_response('abc.html',{'name':name})

from django.template.loader import get_template
def abc(request):
    template = get_template("abc.html")
    name = "hello"
    result = template.render({'name':name})

    return HttpResponse(result)





def tpltest(request,age):
    print(age)
    print(type(age))
    class Say(object):
        def say(self):
            return 'hello'

    name='zs'
    # age=19
    age=int(age)
    hobby=['est','sing','pingpang','football']
    score={'shuxue':89,'yuwen':90,"yingyu":100}
    say=Say()

    # return render(request,'tpltcst.html',{'name':name,'age':age,'hobby':hobby,'score':score})
    return render(request,'tpltest.html',locals())






