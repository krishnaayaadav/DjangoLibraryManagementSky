
from django.contrib import admin
from django.urls import path,include
from employees_app import api_views as views

from rest_framework.routers import DefaultRouter
# Creating Router Object
router = DefaultRouter()
# Register StudentViewSet with Router
router.register('employee/api', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employees_app.urls')),
    path('', include(router.urls)),
    

]
   