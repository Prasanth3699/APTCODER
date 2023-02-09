from django import forms
from .models import Employee


# Employee Form
class EmployeeForm(forms.ModelForm):

    class Meta:
        """Meta definition for Employeeform."""

        model = Employee
        # fields = '__all__'
        fields = ['name', 'address', 'email', 'position', 'company']

        widgets = {
            # 'emp_id':forms.IntegerField(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Employee Name'}),
            'address':forms.Textarea(attrs={'class':'form-control','cols':'30','rows':'2'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'example@mail.com'}),
            'position':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex:FullStack Developer'}),
            'company':forms.Select(attrs={'class':'form-control'}),
        }



