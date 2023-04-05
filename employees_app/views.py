from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages
from django.views import View
from django.db.models import Q 

# Create your views here.

# add employee

def homepage(request):
    all_emp = Employee.objects.all()
    return render(request, 'emp_app/home.html', {'all_emp': all_emp})

def not_found_page(request, *args, **kwargs):
    pass

class AddEmployeeView(View):

    def get(self, request):
        form = EmployeeForm()
        return render(request, 'emp_app/add_employee.html', {'form': form})
    
    def post(self, request):
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congrats New Employee Successfuly Created!')
            return redirect('homepage') # redirecting at home page

        return render(request, 'emp_app/add_employee.html', {'form': form})

class UpdateeEmployee(View):
    def get(self, request,id=None):
            if id is not None and type(id) == int:
                try:
                    emp  = Employee.objects.get(pk=id)
                except Employee.DoesNotExist:
                    return redirect('page_not_found')
                else:
                    form = EmployeeForm(instance=emp)
                    return render(request, 'emp_app/update_employee.html',{'form': form})
            else:
                return redirect('page_not_found')
        
    def post(self, request, id=None):
            if id is not None and type(id) == int:

                try:
                     emp = Employee.objects.get(pk = id)
                except Employee.DoesNotExist:
                     
                     return redirect('page_not_found')
                else:
                    form  = EmployeeForm(request.POST, request.FILES, instance=emp)

                    if form.is_valid():
                         form.save()
                         messages.success(request, 'Employee Data Succeddfuly Updated!')
                         return redirect('homepage')
                    return render(request, 'emp_app/update_employee.html',{'form': form})
                
            else:
                return redirect('page_not_found')
        
class DeleteEmployee(View):
     def get(self, request, id=None):
            if id is not None and type(id) == int:
                try:
                    emp = Employee.objects.get(pk = id)
                except Employee.DoesNotExist:
                     return redirect('page_not_found')
                else:
                    emp.delete()
                    messages.success(request, 'Employee Data Successfuly Deleted!')
                    return redirect('homepage')
            else:
                return redirect('page_not_found')
            

def search_employees(request,id=None, *args, **kwargs):

    search  = request.GET['search']        # getting keywords to search the data
    
    result = Employee.objects.filter(
        Q(name__icontains = search)|       # name contains
        Q(email__icontains=search) |       # email icontains
        Q(salary__icontains = search)|     # salary icontains       
        Q(dept__name__icontains = search)| # dept name icontains
        Q(join_date__icontains = search))  # joining date icontains
    if result.count() <1:                  # checking result is must greater than or equal 1
        result = Employee.objects.all()    # if no object is found than return all obj
         
    return render(request, 'emp_app/home.html', {'all_emp': result})

def dynamic(request, nm=None):
    emp = Employee.objects.all()
   
    if 'recent' in nm:
        emp  = Employee.objects.all().order_by('-join_date')
    
    elif 'max' in nm:
        # emp = Employee.objects.get(pk=1)
        # return render(request, 'emp_app/home.html', {'all_emp': emp})

        all = Employee.objects.all()
        max = 0
        for emps in all:
            if emps.salary>max:
                max = emps.salary
        print(f'\n Maximui salary is: {max} ')
        emp  = Employee.objects.filter(salary__gte = max)
    elif 'min' in nm:
        all = Employee.objects.all()
        salary = all[0].salary # assuming first object has minimium salary
        for em in all:
            if em.salary<salary:
                salary = em.salary
        
        emp   = Employee.objects.filter(salary__lte=salary)
    elif nm is not None:
        emp = Employee.objects.filter(dept__name__icontains=nm)

    if emp.count() < 1:
        emp  = Employee.objects.all()
    return render(request, 'emp_app/home.html', {'all_emp': emp})


