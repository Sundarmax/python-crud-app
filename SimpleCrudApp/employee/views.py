from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from . models import Employee as employee,Department as department
from . serializers import employeeSerializer,departmentSerializer



class Department(APIView):                  # inherits from an APIView
 
    def get(self, request):
        '''
        An API method which returns the all deparments info.
        '''
        obj = department.objects.all()      # Getting all values
        serializer = departmentSerializer(obj, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        ''''
        An API method which is used to add department info. 
        '''
        data = request.data 
        serializer = departmentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

class Employee(APIView):
    
    def get(self, request):
        '''
        An API method which returns the all employees info.
        '''
        obj = employee.objects.all()        # Getting all values 
        serializer = employeeSerializer(obj,many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        ''''
        An API method which is used to add employee info. 
        '''
        data = request.data 
        serializer = employeeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)




