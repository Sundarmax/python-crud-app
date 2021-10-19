from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import Department,Employee

# Name the class as (model name + 'Serializer')

class employeeSerializer(serializers.ModelSerializer):
    class Meta:  
        model = Employee  
        fields = '__all__'

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
