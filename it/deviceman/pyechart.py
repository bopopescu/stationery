from django.db import connection

from django.http import HttpResponse

from django.template import loader

from pyecharts import Bar,Pie
from deviceman.models import pc_list
from django.db.models import Count

REMOTE_HOST = "https://pyecharts.github.io/assets/js"

def exc_sql(sql):

    cursor = connection.cursor()

    cursor.execute(sql)

    result = cursor.fetchall()

    return result

def index(request):

    template = loader.get_template('deviceman/pyecharts.html')

   # b=wbar()
    c=bar()
    #d=lbar()
   # e=dbar()
   # f=sbar()
    i = piebar()
    context = dict(

       # myechart=b.render_embed(),
        wmyechart=c.render_embed(),
        #lmyechart=d.render_embed(),
        #dmyechart=e.render_embed(),
       # smyechart=f.render_embed(),
        ipie=i.render_embed(),
        host=REMOTE_HOST,

        script_list=c.get_js_dependencies()

    )

    return HttpResponse(template.render(context, request))

def bar():

    #_data = []

    query_sql = "select h.name,count(*) from deviceman_pc_list as p,deviceman_hosttype as h where h.id=p.hosttype_id group by hosttype_id"

    data_list = exc_sql(query_sql)
    #data_list=pc_list.objects.values('hosttype__name', 'host_status').annotate(count=Count('host_status')).order_by('hosttype_id')
    x=[i[0] for i in data_list]
   # x = ['sz','bj','gz']

    y=[i[1] for i in data_list]
   # y = [10,20,30]
    #_data.append()

    bar=Bar("设备分类统计",width=700,height=400)

    bar.add("数量",x, y, type="effectScatter", border_color="#ffffff", symbol_size=2,

            is_label_show=True, label_text_color="#0000FF", label_pos="inside", symbol_color="yellow",

            bar_normal_color="#006edd", bar_emphasis_color="#0000ff")



    return bar

def wbar():
    query_sql = "select p.host_status,count(*) from deviceman_pc_list as p where p.hosttype_id=1 group by host_status"

    data_list = exc_sql(query_sql)
    #data_list=pc_list.objects.values('hosttype__name', 'host_status').annotate(count=Count('host_status')).order_by('hosttype_id')
    x=[i[0] for i in data_list]
    #x = ['sz','bj','gz']

    y=[i[1] for i in data_list]
    #y = [10,20,30]
    #_data.append()

    bar=Bar("Workstation",width=400,height=300)

    bar.add("各种状态数量",x, y, type="effectScatter", border_color="#ffffff", symbol_size=2,

            is_label_show=True, label_text_color="#0000FF", label_pos="inside", symbol_color="yellow",

            bar_normal_color="#006edd", bar_emphasis_color="#0000ff")
    return bar

def lbar():
    query_sql = "select p.host_status,count(*) from deviceman_pc_list as p where p.hosttype_id=2 group by host_status"

    data_list = exc_sql(query_sql)
    #data_list=pc_list.objects.values('hosttype__name', 'host_status').annotate(count=Count('host_status')).order_by('hosttype_id')
    x=[i[0] for i in data_list]
    #x = ['sz','bj','gz']

    y=[i[1] for i in data_list]
    #y = [10,20,30]
    #_data.append()

    bar=Bar("Laptop",width=400,height=300)

    bar.add("各种状态数量",x, y, type="effectScatter", border_color="#ffffff", symbol_size=2,

            is_label_show=True, label_text_color="#0000FF", label_pos="inside", symbol_color="yellow",

            bar_normal_color="#006edd", bar_emphasis_color="#0000ff")
    return bar

def dbar():
    query_sql = "select p.host_status,count(*) from deviceman_pc_list as p where p.hosttype_id=3 group by host_status"

    data_list = exc_sql(query_sql)
    #data_list=pc_list.objects.values('hosttype__name', 'host_status').annotate(count=Count('host_status')).order_by('hosttype_id')
    x=[i[0] for i in data_list]
    #x = ['sz','bj','gz']

    y=[i[1] for i in data_list]
    #y = [10,20,30]
    #_data.append()

    bar=Bar("Desktop",width=400,height=300)

    bar.add("各种状态数量",x, y, type="effectScatter", border_color="#ffffff", symbol_size=2,

            is_label_show=True, label_text_color="#0000FF", label_pos="inside", symbol_color="yellow",

            bar_normal_color="#006edd", bar_emphasis_color="#0000ff")
    return bar

def sbar():
    query_sql = "select p.host_status,count(*) from deviceman_pc_list as p where p.hosttype_id=4 group by host_status"

    data_list = exc_sql(query_sql)
    #data_list=pc_list.objects.values('hosttype__name', 'host_status').annotate(count=Count('host_status')).order_by('hosttype_id')
    x=[i[0] for i in data_list]
    #x = ['sz','bj','gz']

    y=[i[1] for i in data_list]
    #y = [10,20,30]
    #_data.append()

    bar=Bar("Server",width=400,height=300)

    bar.add("各种状态数量",x, y, type="effectScatter", border_color="#ffffff", symbol_size=2,

            is_label_show=True, label_text_color="#0000FF", label_pos="inside", symbol_color="yellow",

            bar_normal_color="#006edd", bar_emphasis_color="#0000ff")
    return bar

def piebar():

    #_data = []

    query_sql = "select h.name,count(*) from deviceman_pc_list as p,deviceman_hosttype as h where h.id=p.hosttype_id group by hosttype_id"

    data_list = exc_sql(query_sql)
    #data_list=pc_list.objects.values('hosttype__name', 'host_status').annotate(count=Count('host_status')).order_by('hosttype_id')
    nrows=[i[0] for i in data_list]
   # x = ['sz','bj','gz']

    cols=[i[1] for i in data_list]
   # y = [10,20,30]
    #_data.append()

    pie = Pie("百分比", title_pos='left', width=700, title_text_size=20, page_title='我的柱状图')

    pie.add("", nrows, cols, is_label_show=True, is_legend_show=True, legend_pos="right")

    return pie