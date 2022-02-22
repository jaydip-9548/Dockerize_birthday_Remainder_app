from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

@csrf_exempt 


@permission_classes(IsAuthenticated)
def DemoView(request):
    if request.user.is_authenticated:
        return HttpResponse(request)
    
    return HttpResponse("Not Register")
    
    
    
def logout(request):
    auth.logout(request)
    return HttpResponse("Logout")

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        python_data = JSONParser().parse(request)
        username = python_data['username']
        password = python_data['password']

        user = auth.authenticate(username=username, password=password)
        content_type = 'application/json'

        if user is not None:
            auth.login(request, user)
            response = {
                "id": user.id,
                "isLogin": True,
                "status": "Login Success"
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type=content_type)
            # return redirect('/')

        else:
            response = {
                "status": "Login Failed",
                "isLogin": False
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type=content_type)


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
                "status": "Username already taken !",
                "isregistered": False
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type=content_type)
        elif User.objects.filter(email=email).exists():
            response = {
                "status": "Email is already registered !",
                "isregistered": False
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type=content_type)
        else:
            user = User.objects.create_user(
                first_name=first_name, email=email, username=username, password=password)
            user.save()
            response = {
                "status": "Registration successfull !",
                "isRegistered": True
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type=content_type)