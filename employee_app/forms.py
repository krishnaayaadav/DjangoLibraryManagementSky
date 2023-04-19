from django import forms 
from .models import Employee


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(required= True, error_messages={'required': 'Name is required', 'placeholder': 'Enter name here'})

    def clean_name(self):
        name = str(self.cleaned_data['name'])

        if (len(name) <7):
                raise forms.ValidationError('Name must contains as least 7 characters!')
        
        if ((name.replace(" ", 'a')).isalpha() == False):
            raise forms.ValidationError('Name does not contains numbers or special sysmbols')
        return name
    
    def clean_salary(self):
        salary = self.cleaned_data['salary']

        if salary <10000:
             raise forms.ValidationError('Salary must be greater than 10000')
        return salary
        
            
    class Meta:
        model  = Employee
        fields = ('name', 'email', 'dept', 'salary', 'image')


        error_messages = {
            'image': {'required': 'Image is required'},
            'name': {'required': 'Name is required'},
            'email': {'required': 'Email is required'},
            'salary': {'required': 'Salary is required'},
            'dept': {'required': 'Department is required'}
        }


class SearchForm(forms.Form):
    query = forms.CharField(max_length=250, min_length=2, required=True, widget=forms.TextInput(attrs={'class': 'search', 'placeholder': 'Search something'}))