from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from.models import emp
from django.core.serializers import serialize
# Create your views here.
def call(request):
    data={"name":"sunil","phone_no":123456789,"fb":"none"}
    jason_data=json.dumps(data)
    return HttpResponse(jason_data,content_type="application/json")
class Admin_Registeration(View):
    def get(self,request,id,*args,**kwargs):
        data=emp.objects.get(id=id)
        #######//////////// general get if id = one/////
        # print(data)
        # from_db={"eid":data.id,"ename":data.ename}
        # return JsonResponse(from_db)
        #######/////////// using serializers  $$$$$$$$$$$$$$$$$$(django=>serializer)///////////
        #json_data=serialize("json",[data,])
        ######/only if we want to send specified field/////
        json_data=serialize("json",[data,],fields=("eaddress"))
        print("serializer",json_data)
        return HttpResponse(json_data,content_type="application/json")
class Admin_RegisterationCRD(View):
    def get(self,request,*args,**kwargs):
        data=emp.objects.all()
        json_data=serialize("json",data)
        jason_load=json.loads(json_data)
        files_list=[]
        for q in jason_load:
            files_list.append(q["fields"])
        json_dumps=json.dumps(files_list)
        return HttpResponse(json_dumps,content_type="application/json")