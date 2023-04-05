         
            
from .models import Employee
from .serializers import StudentSerializer
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
  """This class will providing endpoints for get,post,patch and delete only.
      So by using this we can get the data, insert data, update and delete also.
      Welcome by Krishna Thank you for visit
  """
  queryset = Employee.objects.all()
  serializer_class = StudentSerializer
