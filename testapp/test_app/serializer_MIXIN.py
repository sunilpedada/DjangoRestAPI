from django.core.serializers import serialize
from django.http import HttpResponse
import json
class serializer_mixin(object):
    def get_serializer_mixin(self,qs):
        json_data=serialize("json",qs,fields=("ename","eaddress"))
        json_load=json.loads(json_data)
        file_list=[]
        for object in json_load:
            file_list.append(object["fields"])
        json_dump=json.dumps(file_list)
        return json_dump
    def http_response(self,dumpdata,status):
        return HttpResponse(dumpdata,content_type="application/json",status=status)