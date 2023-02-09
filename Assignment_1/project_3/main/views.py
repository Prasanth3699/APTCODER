from django.shortcuts import render
from .forms import EmployeeForm, StudentForm 
# Create your views here.

# Home Page
def home(request):
    return render(request, 'main/index.html')


# Registration Page
def registration(request):
    context = {
        'student':StudentForm,
        'employee':EmployeeForm
    }
    return render(request, 'main/registration.html', context)