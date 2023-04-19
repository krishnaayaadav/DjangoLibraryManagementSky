from django.urls import path
from .views import *  # import all views of employee-app
from .api_views import EmployeeAPIView

from . import api_views
urlpatterns = [
    path('', homepage, name='homepage'),
    path('search/by/',search_employees, name='employeesFilter'),
    path('select/<str:nm>/', dynamic, name='details'),

    path('add-employee/',AddEmployeeView.as_view(), name='addEmployees'),
    path("update-employee/<int:id>/", UpdateeEmployee.as_view(), name="update_employee"),
    path('delete-employee/<int:id>/',DeleteEmployee.as_view(), name='deleteEmployee'),
    
    # api -views 
    # path('api/employee/',api_views.EmployeesAPI.as_view(), name='employee_api'),
    # path('api/employee/<int:id>/',EmployeeAPIView.as_view(), name='employee_api'),
    
    # path('api/department/',api_views.DepartmentAPI.as_view(), name='department-api'),
    # path('api/department/<int:id>/',api_views.DepartmentAPI.as_view(), name='department-api'),

    

]
