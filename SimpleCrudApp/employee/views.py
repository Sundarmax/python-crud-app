from typing import ClassVar
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from . models import Employee as employee,Department as department
from . serializers import employeeSerializer,departmentSerializer



class Department(APIView):                  # inherits from an APIView
 
    def get(self, request,id=None):
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
        if serializer.is_valid():           # Validation
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
        if serializer.is_valid():           # Validation
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)


class DepartmentById(APIView):
    
    def resouce_not_exist(self):
        '''
        A method which raises if an existing record not available in db.
        '''
        return Response({"error": "Not Found"}, status=404)

    def get_object(self, id):
        try:
            return department.objects.get(dept_id = int(id))
        except department.DoesNotExist as e:
            return False

    def get(self,request,id=None):
        ''''
        A method which returns the record by given id. 
        '''
        instance = self.get_object(id)
        if instance:
            serializer = departmentSerializer(instance)
            return Response(serializer.data)
        else:
            return self.resouce_not_exist()

    def put(self,request, id=None):
        ''''
        A method which overrides the existing record
        '''
        data = request.data
        instance = self.get_object(id)
        if instance:
            serializer = departmentSerializer(instance,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors,status=400)
        else:
            return self.resouce_not_exist()


    def delete(self,request,id=None):
        ''''
        A method which deletes the existing record if found. 
        '''
        instance = self.get_object(id)
        if instance:
            serializer = departmentSerializer(instance)
            instance.delete()
            return Response(serializer.data,status=204)
        else:
            return self.resouce_not_exist()

class EmployeeById(APIView):
    
    def resouce_not_exist(self):
        '''
        A method which raises if an existing record not available in db.
        '''
        return Response({"error": "Not Found"}, status=404)

    def get_object(self, id):
        try:
            return employee.objects.get(emp_id = int(id))
        except Exception as e:
            return False
    
    def get(self,request,id=None):
        ''''
        A method which returns the record by given id. 
        '''
        instance = self.get_object(id)
        if instance:
            serializer = employeeSerializer(instance)
            return Response(serializer.data)
        else:
            return self.resouce_not_exist()     

    def put(self,request, id=None):
        ''''
        A method which overrides the existing record
        '''
        data = request.data 
        instance = self.get_object(id)
        if instance:
            serializer = employeeSerializer(instance,data = data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors,status=400)
        else:
            return self.resouce_not_exist()

    def delete(self,request,id=None):
        ''''
        A method which deletes the existing record if found. 
        '''
        instance = self.get_object(id)
        if instance:
            serializer = employeeSerializer(instance)
            instance.delete()
            return Response(serializer.data,status=204)
        else:
            return self.resouce_not_exist()
