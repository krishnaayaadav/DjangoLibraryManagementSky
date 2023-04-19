
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static



from employee_app.api_views import EmployeeAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees/api', EmployeeAPI, basename='employee_api')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee_app.urls')),
    path('', include(router.urls)),
   
    
    

] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
