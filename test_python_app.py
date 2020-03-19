import requests
import json

def requests_function():
    data=requests.get("http://127.0.0.1:8000/api/")
    print(data.json())
def post():
    BASE_URL="http://127.0.0.1:8000/api/"
    ENDPOINT="mixinserializers/"
    data={"ename":"offer","esalary":5,"eaddress":"sklm"}
    json_dumps=json.dumps(data)
    response=requests.post(BASE_URL+ENDPOINT,data=json_dumps)
    print(response.json())
    print(response.status_code)
def update(id):
    update_data={"ename":"gud","esalary":600,"eaddress":"rty"}
    response=requests.put("http://127.0.0.1:8000/api/get_call_1/"+str(id)+"/",data=json.dumps(update_data))
    print(response.json())
    print(response.status_code)
def delete(id):
    response=requests.delete("http://127.0.0.1:8000/api/get_call_1/"+str(id)+"/")
    print(response.json())
    print(response.status_code)
delete(4)
    
