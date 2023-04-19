from .models import Employee
from django.views import View
from django.db.models import Q 
from .forms import EmployeeForm,SearchForm
from django.contrib import messages
from django.shortcuts import render,redirect
from django.core.paginator import Paginator

def homepage(request):
    
    all_emp = Employee.objects.all()
    paginator = Paginator(all_emp, 1, orphans=1) # paginator obj created
    page_number = request.GET.get('page')        
    page_obj    = paginator.get_page(page_number)

    
    return render(request, 'emp_app/home.html', {'page_obj': page_obj})

def search_employees(request,by=None, *args, **kwargs):
    
    query   = ''
    result = Employee.objects.all()
    
    if 'query' in request.GET:
        
        form =    SearchForm(request.GET)    # getting keywords to search the data
        if form.is_valid():
            search = form.cleaned_data.get('query')
        
            result = Employee.objects.filter(
                Q(name__icontains = search)|       # name contains
                Q(email__icontains=search) |       # email icontains
                Q(salary__icontains = search)|     # salary icontains       
                Q(dept__name__icontains = search)| # dept name icontains
                Q(join_date__icontains = search))  # joining date icontains
        
        if result.count()<1:
            result = Employee.objects.all()
    
    p = Paginator(result, 1)
    page_number = 1
    page_obj = p.get_page(page_number)

    return render(request, 'emp_app/home.html', {'page_obj': page_obj })

def dynamic(request, nm=None):
    # defualt return all 
    emp = Employee.objects.all()
   
    if 'recent' in nm:
        emp  = Employee.objects.all().order_by('-id')
    
    elif 'max' in nm:
        # emp = Employee.objects.get(pk=1)
        # return render(request, 'emp_app/home.html', {'all_emp': emp})

        all = Employee.objects.all()
        max = 0
        for emps in all:
            if emps.salary>max:
                max = emps.salary
        # print(f'\n Maximui salary is: {max} ')
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
    
    # creating paginatonation using Paginator class
    p = Paginator(emp, 1, orphans=1)
    page_number  = request.GET.get('page')
    page_obj     = p.get_page(page_number)
    

    return render(request, 'emp_app/home.html', {'page_obj': page_obj})

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
        if request.user.is_superuser:
        
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
        else:
            messages.success(request, "Sorry! You Don't have permissions to delete employees  data! Only Admin(Krishna) Can Delete Data! Thank You!")
            return redirect('homepage')
            
