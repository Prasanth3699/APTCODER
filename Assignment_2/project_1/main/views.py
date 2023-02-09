from django.shortcuts import render
from .models import Company, Employee
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import EmployeeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# Home View
def home(request):
    # company_data = Company.objects.all() #get all company data
    employee_data = Employee.objects.all().order_by('-emp_id') #Fetching Employee Data in reverse order
    total_employees = Employee.objects.all().count() #Total count
    
    # paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(employee_data, 10)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {
        "employees": data,
        "total_employees": total_employees,
        "data_paginator":data,
    }
    return render(request, "main/index.html", context)

# Editing existing employee
def edit_employee(request, emp_id):
    employee = Employee.objects.get(emp_id=emp_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid:
            form.save() #save employee
            return redirect('home')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "main/edit_employee.html", {'form':form})

# Adding New Employee
def add_employee(request):
    form = EmployeeForm()
    
    # to save employee details
    data = EmployeeForm(request.POST)
    if data.is_valid():
        data.save()
        return redirect('home')
    return render(request,"main/add_employee.html",{'form':form})

# Delete Employee Data
def delete_employee(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    employee.delete()
    return redirect("home")
