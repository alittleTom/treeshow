from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import json,time
from yxtest3.models import *
from django.core import serializers
from yxtest3.util import  CJsonEncoder
import os

# Create your views here.

def getRequirementById(id):
    try:
        return requirement.objects.get(id=id)
    except requirement.DoesNotExist:
        return None
def getRequirementByName(name):
    try:
        return requirement.objects.filter(name__contains=name)
    except requirement.DoesNotExist:
        return None

def getAllRequirement():
    return requirement.objects.all()

def getTestById(id):
    try:
        return test.objects.get(id=id)
    except test.DoesNotExist:
        return None


def getAllTest():
    return test.objects.all()

def getScriptById(id):
    try:
        return scriptVersion.objects.get(id=id)
    except:
        return None

def getAllScript():
    return scriptVersion.objects.all()

#返回的是个list
def getRequirementTableMessage(request):
    limit = int(request.GET['limit'])
    offset = int(request.GET['offset'])
    requirement_queryset=getAllRequirement()[offset:(offset+limit)]
    require_list=[]
    for item in requirement_queryset:
        root=getRequirementById(item.root)
        if(root==None):
            rootname='无'
        else:
            rootname=root.name
        if(getRequirementById(item.pre)):
            prename = getRequirementById(item.pre).name
        else:
            prename='无'
        status=statusToString(item.status)
        #dict={'name':item.name,'id':item.id,'time':item.time,'root':root_dict,'pre':pre_dict,'status':status}
        dict = {'name': item.name, 'id': item.id, 'time': item.time, 'rootname': rootname, 'prename': prename,
                'status': status}
        require_list.append(dict)
    num = str(requirement.objects.count())
    json_data = json.dumps(require_list, cls=CJsonEncoder.CJsonEncoder)
    jsonstr = "{\"total\":" + num + ",\"rows\":" + json_data + "}"
    return jsonstr

def getTestTableMessage(request):
    limit = int(request.GET['limit'])
    offset = int(request.GET['offset'])
    test_queryset=getAllTest()[offset:(offset+limit)]
    test_list=[]
    for item in test_queryset:
        req=getRequirementById(item.requirement_id)
        if(req==None):
            require='无'
        else:
            require=req.name
        status=statusToString(item.status)
        dict={'id':item.id,'name':item.name,'creator':item.creator,'doc':item.doc.name,'time':item.time,'status':status,'requirement':require}
        test_list.append(dict)
    num = str(test.objects.count())
    json_data = json.dumps(test_list, cls=CJsonEncoder.CJsonEncoder)
    jsonstr = "{\"total\":" + num + ",\"rows\":" + json_data + "}"
    return jsonstr

def getScriptTableMessage(request):
    limit = int(request.GET['limit'])
    offset = int(request.GET['offset'])
    script_queryset=getAllScript()[offset:(offset+limit)]
    script_list=[]
    for item in script_queryset:
        test=getTestById(item.test_id)
        if(test==None):
            testMessage='无'
        else:
            testMessage=test.name
        dict={'id':item.id,'name':item.name,'creator':item.creator,'doc':item.doc.name,'time':item.time,'test':testMessage,'remark':item.remarks}
        script_list.append(dict)
    num = str(scriptVersion.objects.count())
    json_data = json.dumps(script_list, cls=CJsonEncoder.CJsonEncoder)
    jsonstr = "{\"total\":" + num + ",\"rows\":" + json_data + "}"
    return jsonstr

def messagetest(request):
    #return HttpResponse({'requirement':requirement_list,'script':script_list,'test':test_list})
    return render_to_response('yxtest3Html/t1.html')


def requirementtable(request):
    requirementJson = getRequirementTableMessage(request)
    return HttpResponse(requirementJson)
def testtable(request):
    testJson = getTestTableMessage(request)
    return HttpResponse(testJson)
def scripttable(request):
    scriptJson = getScriptTableMessage(request)
    return HttpResponse(scriptJson)

def requirementQuery(request,name):
    requirement_queryset=getRequirementByName(name)
    if(requirement_queryset==None):
        return render_to_response('yxtest3Html/requirementTable.html')
    else:
        require_list = []
        for item in requirement_queryset:
            root = getRequirementById(item.root)
            root_dict = {'name': root.name, 'id': root.id}
            if (item.pre == 0):
                pre_dict = {'name': '无', 'id': 1}
            else:
                pre = getRequirementById(item.pre)
                pre_dict = {'name': pre.name, 'id': pre.id}
            status = statusToString(item.status)
            dict = {'name': item.name, 'id': item.id, 'time': item.time, 'root': root_dict, 'pre': pre_dict,
                    'status': status}
            require_list.append(dict)
        return render_to_response('yxtest3Html/requirementTable.html',{'requirement':require_list})
def statusToString(status):
    if(status==1):
        return '已完成'
    else:
        return '未完成'

def gettable(request):
    limit=int(request.GET['limit'])
    offset=int(request.GET['offset'])
    req_list=getAllRequirement()[offset:(offset+limit)]
    require_list = []
    for item in req_list:
        root = getRequirementById(item.root)
        root_dict = root.name
        if (item.pre == 0):
            pre_dict = '无'
        else:
            pre = getRequirementById(item.pre)
            pre_dict =  pre.name
        status = statusToString(item.status)
        # dict={'name':item.name,'id':item.id,'time':item.time,'root':root_dict,'pre':pre_dict,'status':status}
        dict = {'name': item.name, 'id': item.id, 'time': item.time, 'rootname': root_dict, 'prename': pre_dict,
                'status': status}
        require_list.append(dict)
    print(require_list)
    json_data=json.dumps(require_list,cls=CJsonEncoder.CJsonEncoder)
    num=str(requirement.objects.count())
    jsonstr="{\"total\":" + num + ",\"rows\":" + json_data + "}"
    return HttpResponse(jsonstr,content_type="application/json")

def requirementtemplates(request):
    return render_to_response('yxtest3Html/requirementTable.html')
def testtemplate(request):
    return render_to_response('yxtest3Html/testTable.html')
def scripttemplate(request):
    return render_to_response('yxtest3Html/scriptTable.html')

def requirementadd(request):
    requirementSet = requirement.objects.all()
    dic = {}
    for item in requirementSet:
        dic[item.id] = item.name
        print(item.name, item.id)
    return render_to_response('yxtest3Html/addrequirement.html',{'requirementSet': dic})
def requirementadd_submit(request):
    name = request.POST['name']
    time=request.POST['time']
    root_id=int(request.POST['root'])
    pre_id=int(request.POST['pre'])
    status=int(request.POST['status'])
    dic={'name':name,'time':time,'root':root_id,'pre':pre_id,'status':status}
    requirement.objects.create(**dic)
    return HttpResponse(json.dumps('创建成功'))

def testadd(request):
    requirement_id = request.GET['requirement_id']
    requirement_name=request.GET['requirement_name']
    dic={'requirement_id':requirement_id,'requirement_name':requirement_name}
    return render_to_response("yxtest3Html/testaddtemplate.html",{'dic':dic} )

def testaddsubmit(request):
    register(request)
    name = request.POST['name']
    doc =  request.POST['doc']
    creator = request.POST['creator']
    time=request.POST['time']
    status = int(request.POST['status'])
    requirement_id = request.POST['requirement_id']
    dic = {'name': name, 'doc': doc, 'creator': creator, 'time': time, 'status': status,
           'requirement_id': requirement_id}
    test.objects.create(**dic)
    return HttpResponse(json.dumps('创建成功'))

def scriptadd(request):
    #print (request.GET)
    test_id = request.GET['test_id']
    test_name=request.GET['test_name']
    dic={'test_id':test_id,'test_name':test_name}
    return render_to_response('yxtest3Html/addscript.html',{'dic':dic})

def scriptadd_submit(request):
    register(request)
    name = request.POST['name']
    time=request.POST['time']
    doc=request.POST['doc']
    remarks=request.POST['remarks']
    creator=request.POST['creator']
    test_id=request.POST['test_id']
    dic={'name':name,'time':time,'doc':doc,'remarks':remarks,'creator':creator,'test_id':test_id}
    scriptVersion.objects.create(**dic)
    return HttpResponse(json.dumps('创建成功'))

def register(request):
    if request.method == 'POST':
        #一些操作。。。。。。。。
        # 保存上传的文件
        myFile = request.FILES.get("filePath", None)
        print(myFile)
        destination = open(os.path.join("upload/yxtest3/test", myFile.name), 'wb+') # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks(): # 分块写入文件
            destination.write(chunk)
        destination.close()
