from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.db import connection, connections, transaction
from treeShowMessage.models import *
import json


# Create your views here.

# 测试执行自定义sql
def executeSql(request):
    cursor = connections['oracle'].cursor()
    cursor.execute("select * from rwd_core_param")
    transaction.commit()
    list = cursor.fetchall()
    print(type(list))
    print(list)
    return HttpResponse("ok")


# 开发多算酬金
def kf_more_cj(mxname, date):
    print('--'+mxname)
    cjname = get_cj_nama(mxname)
    kf_cj_table_name = get_kf_cj_table(mxname, date)
    cs_cj_table_name = get_cs_cj_table(cjname)
    print(cjname)
    print(kf_cj_table_name)
    print(cs_cj_table_name)
    print(date)
    if (cs_cj_table_name == None):
        list = []
        dic = {}
        dic['主键1'] = '无'
        dic['主键2'] = '无'
        dic['酬金'] = '没有该酬金表'
        dic['渠道编码'] = '无'
        list.append(dic)
        json_data = json.dumps(list, ensure_ascii=False)
        jsonstr = "{\"total\":" + '1' + ",\"rows\":" + json_data + "}"
        return jsonstr
    else:
        cursor = connections['oracle'].cursor()
        sql = "select data_id 主键1,data2_id 主键2,stat_VAL 酬金,LINK_ID 渠道编码 from " + kf_cj_table_name + " a where a.id= %s minus select to_char(BILL_ID), to_char(ID),to_char(CJ),to_char(CHNL_CODE) from " + cs_cj_table_name + " a where a.id= %s and a.value_month= %s"
        data = [mxname, cjname, date]
        cursor.execute(sql, data)
        transaction.commit()
        return resultToJson(cursor.fetchall())
# 测试多算酬金
def cs_more_cj(mxname, date):
    cjname = get_cj_nama(mxname)
    kf_cj_table_name = get_kf_cj_table(mxname, date)
    cs_cj_table_name = get_cs_cj_table(cjname)
    if (cs_cj_table_name == None):
        list = []
        dic = {}
        dic['主键1'] = '无'
        dic['主键2'] = '无'
        dic['酬金'] = '没有该酬金表'
        dic['渠道编码'] = '无'
        list.append(dic)
        json_data = json.dumps(list, ensure_ascii=False)
        jsonstr = "{\"total\":" + '1' + ",\"rows\":" + json_data + "}"
        return jsonstr
    else:
        cursor = connections['oracle'].cursor()
        sql = "select to_char(BILL_ID) 主键1, to_char(ID) 主键2,to_char(CJ) 酬金,to_char(CHNL_CODE) 渠道编码 from " + cs_cj_table_name + " a where a.id= %s and a.value_month=%s minus select data_id,data2_id,stat_VAL,LINK_ID from " + kf_cj_table_name + " a where a.id=%s"
        data = [cjname, date, mxname]
        cursor.execute(sql, data)
        transaction.commit()
        return resultToJson(cursor.fetchall())


# 返回拼接好的开发酬金表
def get_kf_cj_table(cjname, date):
    cursor = connections['oracle'].cursor()
    cursor.execute("select sch_id from rwd_core_param a where a.code= %s ", [cjname])
    transaction.commit()
    name = cursor.fetchone()[0]
    print(name + '_' + date + '_mz')
    return name + '_' + date + '_mz'

# 返回测试的酬金表
def get_cs_cj_table(cjname):
    if (cjname == ""):
        return None
    else:
        return rwd_kmk_cjhz.objects.using('oracle').get(酬金名称=cjname).酬金结果表


# 根据明细name得到酬金name
def get_cj_nama(name):
    return rwd_kmk_cjhz.objects.using('oracle').get(mingxi=name).酬金名称


# 取到的结果元组封装成json
def resultToJson(tuple):
    list = []
    for i in range(len(tuple)):
        dic = {}
        dic['主键1'] = tuple[i][0]
        dic['主键2'] = tuple[i][1]
        dic['酬金'] = tuple[i][2]
        dic['渠道编码'] = tuple[i][3]
        list.append(dic)
    num = str(len(tuple))
    json_data = json.dumps(list, ensure_ascii=False)
    jsonstr = "{\"total\":" + num + ",\"rows\":" + json_data + "}"
    return jsonstr


def getkftable(request):
    date = str(request.GET['date']).replace('-', '')
    mxname = request.GET['mxname']
    # limit=request.GET['limit']
    # offset=request.GET['offset']
    # 分页功能未实现
    return HttpResponse(kf_more_cj(mxname, date))
def getcstable(request):
    date = str(request.GET['date']).replace('-', '')
    mxname = request.GET['mxname']
    return HttpResponse(cs_more_cj(mxname,date))