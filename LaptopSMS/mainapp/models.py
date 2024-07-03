from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string


class User(AbstractUser):
    terms_accepted = models.BooleanField(default=False)
    profile_img = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='profile_pics/default.jpg')  
    
    def __str__(self):
        return self.username
    
class Customer(models.Model):
    customerName = models.CharField(max_length=100)
    customerEmail = models.EmailField()
    customerMobNo = models.BigIntegerField()
    customerAddress = models.TextField()
    
    def __str__(self):
        return self.customerName
    
# Product Inward Model
class ProductInward(models.Model):
    serialNo = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    problem = models.TextField()
    remark = models.TextField()
    inwardDate = models.DateTimeField(auto_now_add=True)
    commitmentDate = models.DateField()
    productStatus = models.CharField(max_length=30)
    productChecked = models.BooleanField(default=False)
    
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True ,related_name='product_inward')

    def __str__(self):
        return self.serialNo

class Team(models.Model):
    empName = models.CharField(max_length=100)
    empEmail = models.EmailField()
    empMobNo = models.BigIntegerField()
    empDOB = models.DateField()
    salary = models.FloatField()
    
    is_active = models.BooleanField(default=True)
    
    position = models.CharField(max_length=30, choices=[
        ('Laptop Technician', 'Laptop Technician'),
        ('Computer Technician', 'Computer Technician'),
        ('Chip-level Technician', 'Chip-level Technician'),
        ('Manager', 'Manager'),
        ('HR', 'HR'),
        ('Other Staff', 'Other Staff')], null=False)
    empTerms = models.BooleanField(default=False)
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
    
#Service model
class Service(models.Model):
    service_id = models.CharField(max_length=7, unique=True, editable=False)
    component = models.CharField(max_length=100, null=True)
    serviceRemark = models.CharField(max_length=100)
    serviceStatus = models.CharField(max_length=30)
    serviceCost = models.FloatField()
    serviceDate = models.DateField(auto_now=True)
    
    serviceTechnician = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='serviceTechnician')
    product = models.ForeignKey(ProductInward, on_delete=models.SET_NULL, null=True ,related_name='service')
    
    def __str__(self):
        return f"Service ID: {self.service_id}"
    
    def save(self, *args, **kwargs):
        if not self.service_id:
            self.service_id = self.generate_unique_id()
        super().save(*args, **kwargs)

    def generate_unique_id(self):
        while True:
            random_digits = ''.join(random.choices(string.digits, k=4))
            service_id = f"SER{random_digits}"
            if not Service.objects.filter(service_id=service_id).exists():
                return service_id


class Delivery(models.Model):
    product = models.ForeignKey(ProductInward, on_delete=models.SET_NULL, null=True ,related_name='product')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True ,related_name='service')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True ,related_name='Customer')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True ,related_name='team')
    
    deliveryDate = models.DateTimeField(auto_now_add=True)
    
    customerSatisfaction = models.CharField(max_length=20, choices=[
        ('Satisfied', 'Satisfied'),
        ('Neutral', 'Neutral'),
        ('Not Satisfied', 'Not Satisfied')
    ], null=True, blank=True)
    
    deliveredOnTime = models.CharField(max_length=20, choices=[
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], null=True, blank=True)
    