from django.shortcuts import render,HttpResponse,render_to_response
from treeShowMessage.models import *
import json
from django.forms.models import model_to_dict
# Create your views here.
def getdatatest(request):
    return render_to_response('treeShowMessage/tree.html')

def gettreedata(request):
    list=rwd_kmk_cjhz.objects.using('oracle').all()
    treedata=[]
    for item in list:
        first=judgeInTreeList(item.kemu, treedata)
        if(first["boolean"]!=True):
            addnodes(item.kemu,treedata)
            first = judgeInTreeList(item.kemu, treedata)

        second=judgeInTreeList(item.huizong2, first["node"])
        if(second["boolean"]!=True):
            addnodes(item.huizong2,first["node"])
            second = judgeInTreeList(item.huizong2, first["node"])

        third=judgeInTreeList(item.huizong1,second["node"])
        if(third["boolean"]!=True):
            addnodes(item.huizong1,second["node"])
            third=judgeInTreeList(item.huizong1,second["node"])


        fourth=judgeInTreeList(item.mingxi,third["node"])
        if(fourth["boolean"]!=True):
            #dic4 = {"text": item.mingxi,"tags":['available']}"href": "showInfo?q="+item.mingxi
            dic4 = {"text": item.mingxi}
            third["node"].append(dic4)
    return HttpResponse(json.dumps(treedata,ensure_ascii=False))
def judgeInTreeList(name,list):
    for item in list:
        if(name==item['text']):
            return {"boolean":True,"node":item['nodes']}
    return {"boolean":False}

def addnodes(name,list):
    dic={"text":name,"nodes":[]}
    list.append(dic)

def showInfo(request):
    mingxi=request.GET['q']
    message=rwd_kmk_cjhz.objects.using('oracle').get(mingxi=mingxi)
    message_dic=model_to_dict(message)
    return HttpResponse(json.dumps(message_dic,ensure_ascii=False))
