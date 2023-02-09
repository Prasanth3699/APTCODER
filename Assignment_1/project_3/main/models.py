from django.db import models

# Create your models here.
class Employee(models.Model):
    """Model definition for Employee."""

    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_details = models.IntegerField()
    email = models.EmailField(unique=True)

    class Meta:
        """Meta definition for Employee."""

        verbose_name = 'Employee'
        

    def __str__(self):
        """Unicode representation of Employee."""
        return self.emp_id

class Student(models.Model):
    """Model definition for Student."""

    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_details = models.IntegerField()
    email = models.EmailField(unique=True)

    class Meta:
        """Meta definition for Student."""

        verbose_name = 'Student'
       

    def __str__(self):
        """Unicode representation of Student."""
        return self.student_id
