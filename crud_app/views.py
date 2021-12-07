from django.shortcuts import render
from rest_framework.utils import serializer_helpers
from .models import User
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def createUser(request):
    try:
        if request.method == 'POST' and request.body:
            body = json.loads(request.body)
            # name = data.get('name')
            # age = data.get('age')
            # address = data.get('address')
            data = body.get("records", [])
            print(data)
            obj_list = [User(**data) for data in data]
            print(obj_list)
            p = User.objects.bulk_create(obj_list)
            print(p)
            return HttpResponse("Success 1 ")
    except Exception as e:
        print("Success : 0 Error = {}".format(str(e)))
        return HttpResponse("Success 0 ")
        
@csrf_exempt
def deleteUser(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            name = data.get('name')
            p = User.objects.filter(name=name).delete()
            print(p)
            return HttpResponse("Success 1 ")

    except Exception as e:
        print("Success : 0 Error = {}".format(str(e)))
        return HttpResponse("Success 0 ")




@csrf_exempt
def updateUser(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            name = data.get('name')
            age = data.get('age')
            address = data.get('address')
            p = User.objects.filter(name=name).update(name = name, age =age, address = address)
            return HttpResponse("Success 1 ")

    except Exception as e:
        print("Success : 0 Error = {}".format(str(e)))
        return HttpResponse("Success 0 ")   


@csrf_exempt
def viewAllUsers(request):
    if request.method == 'GET':
        try:
            p = User.objects.all()
            
            data = json.dumps({"DATA": [x.toDict() for x in p]})
            return JsonResponse(data, safe=False)      

        except Exception as e:
            print("Success : 0 Error = {}".format(str(e)))
            return HttpResponse("Success 0 ")

# Create your views here.




