
from rest_framework import serializers
from .models import Employee,Department


class EmployeeSerializer(serializers.ModelSerializer):
   class Meta:
      model  = Employee
      fields = ('id', 'name',   'salary', 'join_date', 'image' )
      

class DepartmentSerializer(serializers.ModelSerializer):
   
   employees = EmployeeSerializer()
   
   class Meta:
      model = Department
      fields = ('id', 'name', 'employees')