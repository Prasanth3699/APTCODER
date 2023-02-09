from django.db import models

# Create your models here.

class Company(models.Model):
    """Model definition for Company."""

    company_id = models.AutoField(primary_key=True)
    domain = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        """Meta definition for Company."""

        verbose_name = 'Company'
    
    def __str__(self):
        """Unicode representation of Company."""
        return str(self.company_id)

class Employee(models.Model):
    """Model definition for Employee."""

    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    class Meta:
        """Meta definition for Employee."""

        verbose_name = 'Employee'

    def __str__(self):
        """Unicode representation of Employee."""
        return self.name
