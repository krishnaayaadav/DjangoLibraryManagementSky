from .models import Employee,Department
from .serializers import EmployeeSerializer,DepartmentSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class EmployeeAPI(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

class EmployeesAPI(APIView):
    # post to use to insert data into datbase
    def post(self, request, format=None):
        """POST request for insert data/records into database Only FOR Authenticated Users  """
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'Inseretd Successfuly': serializer.data}
            return Response(res, status = status.HTTP_201_CREATED)
        else:
            res = {'Error': 'Invalid request'}
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    # fetch data from database
    def get(self, request, format=None):
        """GET request for all kind od users to fetch the data/records"""
        all_emp = Employee.objects.all()
        serializer = EmployeeSerializer(all_emp, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

class EmployeeAPIView(APIView):
    """This class is prodive all features like fetch data,inserting data, update and deletion.
       Thank You Open Any Suggestion krishnapb7431@gmail.com
       """
    # basic authentication classes applied here 
    # authentication_classes = [BasicAuthentication]
    # rest_framework permission class is applied here as IsAuthenticated
    # permission_classes = [IsAuthenticatedOrReadOnly]  # overriding global permission class herem

    # fetch data from database
    def get(self, request,id , format=None):
        """GET request for all kind od users to fetch the data/records"""
        # id  = request.data.get('id', None)

        if not id:
            res={'detail': "Employee is required"}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            try:
                emp = Employee.objects.get(pk = id)
            except Employee.DoesNotExist:
                res={'detail': "Employee Not Exist With this id",}
                return Response(res, status=status.HTTP_204_NO_CONTENT)
            
            else:
                serializer = EmployeeSerializer(emp)
                return Response(serializer.data, status = status.HTTP_200_OK)
    
    # update patch request for partialy update
    def patch(self, request, id, format=None):
        """PATCH request for update data/records into database Only FOR Authenticated Users  """

        if id is not None:
            try:
                emp = Employee.objects.get(pk = id)
            except Employee.DoesNotExist:
                res={'detail': "Employee Not Exist With this id",}
                return Response(res, status=status.HTTP_204_NO_CONTENT)
            
            else:
                serializer = EmployeeSerializer(emp, data  = request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    res = {'Update Successfuly': serializer.data}
                    return Response(res, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
        else:
            res={'detail': "Employee is required for"}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        
     # update patch request for partialy update
    
    # for complete updatoin
    def put(self, request, id, format=None):
        """PUT  request for  complete update data/records into database Only FOR Authenticated Users  """

        
        if id is not None:
            try:
                emp = Employee.objects.get(pk = id)
            except Employee.DoesNotExist:
                res={'detail': "Employee Not Exist that your looking  for"}
                return Response(res, status=status.HTTP_204_NO_CONTENT)
            else:
                serializer = EmployeeSerializer(emp, data  = request.data)
                if serializer.is_valid():
                    serializer.save()
                    res = {'Update Successfuly': serializer.data}
                    return Response(res, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
        else:
            res={'detail': "Employee is required for"}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format = None):
        """DELETE request for delete existing data/records into database Only FOR Authenticated Users  """

        if id:
            try: 
                emp = Employee.objects.get(pk = id)
            except Employee.DoesNotExist: 
                res={'detail': "Employee Not Exist that your looking  for"}
                return Response(res, status=status.HTTP_400_BAD_REQUEST)
            
            else:
                emp.delete() #  deleting employee here
                res = {'Deleted Successfuly': 'Employee Successfuly Deleted'}
                return Response(res, status = status.HTTP_204_NO_CONTENT)
        else:
            res = {'Id required': 'Employee Id is required to delete the data'}
            return Response(res, status = status.HTTP_400_BAD_REQUEST)
        
class DepartmentAPI(APIView):
    
    # fetch data from database
    def get(self, request, id=None, format=None):
        """GET request for all kind od users to fetch the data/records"""
        if not id:
            all_emp = Department.objects.all()
            serializer = DepartmentSerializer(all_emp, many=True)
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            try:
                emp = Department.objects.get(pk = id)
            except Department.DoesNotExist:
                res={'detail': "Employee Not Exist With this id",}
                return Response(res, status=status.HTTP_204_NO_CONTENT)
            
            else:
                serializer = DepartmentSerializer(emp)
                return Response(serializer.data, status = status.HTTP_200_OK)
    
