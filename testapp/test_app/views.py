from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from.models import emp
from django.core.serializers import serialize
from.serializer_MIXIN import serializer_mixin
from.utils import is_json
from.forms import employeesforms
# Create your views here.
#to disable csrf token at method level and functional
#//use from django.views.decorators.csrf import csrf_exempt
#to class level 
#//use from django.views.decorators.csrf import csrf_exempt
# //from django.utils.decorators import method_decorator
# //@method_decorator(csrf_exempt,name="dispaich") 
def call(request):
    data={"name":"sunil","phone_no":123456789,"fb":"none"}
    jason_data=json.dumps(data)
    return HttpResponse(jason_data,content_type="application/json")
class Admin_Registeration(serializer_mixin,View):
    def get(self,request,id,*args,**kwargs):
        # data=emp.objects.get(id=id)
        #######//////////// general get if id = one/////
        # print(data)
        # from_db={"eid":data.id,"ename":data.ename}
        # return JsonResponse(from_db)
        #######/////////// using serializers  $$$$$$$$$$$$$$$$$$(django=>serializer)///////////
        #json_data=serialize("json",[data,])
        ######/only if we want to send specified field/////
        # json_data=serialize("json",[data,],fields=("eaddress"))
        # print("serializer",json_data)
        try:
            qs=emp.objects.get(id=id)
        except emp.DoesNotExist:
            json_data=json.dumps({"msg":"enter valid id"})
        else:
            json_data=self.get_serializer_mixin([qs,])
        return HttpResponse(json_data,content_type="application/json")
    def put(self,request,id,*args,**kwargs):
        try:
            emp_data=emp.objects.get(id=id)
        except emp.DoesNotExist:
            emp_data=None
        if emp_data==None:
            ERROR_MSG=json.dumps({"msg":"not exists"})
            return HttpResponse(ERROR_MSG,status=400)
        request_body_data=request.body
        valid=is_json(request_body_data)
        if not valid:
            msg=json.dumps({"msg":"entered invalid data"})
            return self.http_response(msg,status=400)
        json_load=json.loads(request_body_data)
        print("emp_data",emp_data.ename)
        original_data={"ename":emp_data.ename,
                        "esalary":emp_data.esalary,
                        "eaddress":emp_data.eaddress}
        original_data.update(json_load)
        print("original data",original_data)
        form=employeesforms(original_data,instance=emp_data)
        print("forms data",form)
        if form.is_valid():
            form.save(commit=True)
            qs=emp.objects.get(id=id)
            json_data=self.get_serializer_mixin([qs,])
            return self.http_response(json_data,status=200)
        if form.errors:
            msg=json.dumps(form.errors)
            return self.http_response(msg,status=400)
    def delete(self,request,id,*args,**kwargs):
        try:
            user_details=emp.objects.get(id=id)
            print("user details",user_details)
        except emp.DoesNotExist:
            user_details=None 
        print("user details",user_details)
        if user_details==None:
            msg=json.dumps({"msg":"user not exist"})
            return HttpResponse(msg,status=400)
        status_code,msg=user_details.delete()
        if status_code==1:
            success=json.dumps({"msg":"deleted successfuly"})
            return HttpResponse(success,status=200)
        msg=json.dumps({"msg":"unable to delete"})
        return HttpResponse(msg,status=400)
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
class mixin_serializer(serializer_mixin,View):
    def get(self,request,*args,**kwargs):
        qs=emp.objects.all()
        datas=self.get_serializer_mixin(qs)
        return HttpResponse(datas,content_type="application/json")
    # def post(self,request,*args,**kwargs):
    #     data=request.body
    #     valid=is_json(data)
    #     if not valid:
    #         msg=json.dumps({"msg":"entered invalid data"})
    #         return self.http_response(msg,status=400)
    #     try:
    #         json_load=json.loads(data)
    #         db_data=emp(ename=json_load["ename"],esalary=json_load["esalary"],eaddress=json_load["eaddress"])
    #         db_data.save()
    #         print("fffff",json_load["ename"])
    #         qs=emp.objects.get(ename=json_load["ename"])
    #         data_db=self.get_serializer_mixin([qs,])
    #     except ValueError:
    #         return self.http_response(status=400)
    #     return self.http_response(data_db,status=200)
    ############ implementing by forms########
    def post(self,request,*args,**kwargs):
        data=request.body
        valid=is_json(data)
        if not valid:
            msg=json.dumps({"msg":"entered invalid data"})
            return self.http_response(msg,status=400)
        json_load=json.loads(data)
        forms=employeesforms(json_load)
        if forms.is_valid():
            forms.save(commit=True)
            qs=emp.objects.get(ename=json_load["ename"])
            data_db=self.get_serializer_mixin([qs,])
            return self.http_response(data_db,status=200)
        if forms.errors:
            msg=json.dumps(forms.errors)
            return self.http_response(msg,status=400)