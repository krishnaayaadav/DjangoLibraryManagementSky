from django.urls import path
from .views import *  # import all views of employee-app

urlpatterns = [
    path('', homepage, name='homepage'),
    path('search/by/',search_employees, name='employeesFilter'),
    path('select/<str:nm>/', dynamic, name='details'),

    path('add-employee/',AddEmployeeView.as_view(), name='addEmployees'),
    path("update-employee/<int:id>/", UpdateeEmployee.as_view(), name="update_employee"),
    path('delete-employee/<int:id>/',DeleteEmployee.as_view(), name='deleteEmployee'),
   

]
