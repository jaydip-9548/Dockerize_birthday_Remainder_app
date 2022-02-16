from django.shortcuts import render
from .models import remainderData
from .serializer import remainderDataSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@csrf_exempt
# Allow this methods 
# @api_view(['GET','POST','DELETE','PATCH','UPDATE'])
# Authentication purpose
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def remainder_details(request):
    if request.method == 'GET':
        # get the all model objects
        remainder = remainderData.objects.all()
        # Complex data to python data conversion
        serializer = remainderDataSerializer(remainder,many=True)
        # rendering python datatype to json data types
        json_data = JSONRenderer().render(serializer.data)
        # print(json_data)
        return HttpResponse(json_data,content_type='application/json')
    
    elif request.method == 'POST':
        python_data = JSONParser().parse(request)
        serializer = remainderDataSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Data inserted successfully")
        return HttpResponse("Failed to insert")
        
    elif request.method == 'PUT':
        python_data = JSONParser().parse(request)
        id = python_data.get('id')
        remainder = remainderData.objects.get(id = id)
        serializer = remainderDataSerializer(remainder,data=python_data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("updation success !!")
        return HttpResponse("Failed to update")
    
    elif request.method == 'DELETE':
        python_data = JSONParser().parse(request)
        id = python_data.get('user_id')
        remainder = remainderData.objects.get(user_id = id)
        remainder.delete()
        return HttpResponse("Record Deleted success !!")
        

        
    
        