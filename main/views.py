from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee

def home(request):
    return render(request, "main/home.html")

def employee_data(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['emp_name']
            salary = form.cleaned_data['emp_salary']
            emp = Employee.objects.create(emp_name=name, emp_salary=salary)
            emp.save()
            return HttpResponse("The data is saved in database")
    else:
        form = EmployeeForm()  # Aquí se inicializa `form` para solicitudes que no sean POST
        
    return render(request, 'main/employee.html', {'form': form})
