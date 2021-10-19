from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee,Department as dept
from . serializers import employeeSerializer,departmentSerializer



class Department(APIView):                  # inherits from an APIView
 
    def get(self, request):
        obj = dept.objects.all()      # Getting all values
        serializer = departmentSerializer(obj, many=True)
        return Response(serializer.data, status=200)
