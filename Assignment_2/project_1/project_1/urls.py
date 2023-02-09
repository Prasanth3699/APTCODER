from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('delete_employee/int<emp_id>', views.delete_employee, name='delete_employee'),
    path('edit_employee/int<emp_id>', views.edit_employee, name='edit_employee'),
    path('add_employee', views.add_employee, name='add_employee'),
]
