from django.shortcuts import render,redirect
from .models import userData
from .serializers import userDataSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User,auth
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,authentication_classes,permission_classes

@csrf_exempt
# Allow this methods 


def user_login(request):
    if request.method =='POST':
        python_data = JSONParser().parse(request)
        username = python_data['username']
        password = python_data['password']
        
        user = auth.authenticate(username=username,password=password)
        content_type = 'application/json'

        if user is not None:
            auth.login(request,user)
            response = {
                "id": user.id,
                "isLogin":True,
                "status":"Login Success"
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data,content_type=content_type)
            # return redirect('/')
            
        else:
            response = {
                "status":"Login Failed",
                "isLogin":False
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data,content_type=content_type)

def user_register(request):

    if request.method == 'POST':       
        python_data = JSONParser().parse(request)
        first_name = python_data['first_name']
        email = python_data['email']
        username = python_data['username']
        password = python_data['password']
        content_type = 'application/json'
        
        if User.objects.filter(username=username).exists():
            response = {
                "status":"Username already taken !",
                "isregistered":False
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data,content_type = content_type)
        elif User.objects.filter(email=email).exists():
            response = {
                "status":"Email is already registered !",
                "isregistered":False
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data,content_type = content_type)
        else:
         user = User.objects.create_user(first_name = first_name, email = email , username = username , password = password)
         user.save()
         response = {
                "status":"Registration successfull !",
                "isRegistered":True
            }
         json_data = JSONRenderer().render(response)
         return HttpResponse(json_data,content_type = content_type)
        
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])       
def userRegister(request):
    print(request.user.is_active)
    return HttpResponse('success')