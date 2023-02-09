from django import forms
from .models import Employee, Student


# Employee Form
class EmployeeForm(forms.ModelForm):
    """Form definition for Employee."""

    class Meta:
        """Meta definition for Employeeform."""

        model = Employee
        fields = '__all__'

# Student Form
class StudentForm(forms.ModelForm):
    """Form definition for Student."""

    class Meta:
        """Meta definition for Studentform."""

        model = Student
        fields = '__all__'

