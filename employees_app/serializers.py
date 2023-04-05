
from rest_framework import serializers
from .models import Employee

# StudentSerializer class
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  Employee
        fields = ('id', 'name','email', 'salary', 'dept', 'email','join_date', 'image')
