from email import message, policy
import email
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email=models.EmailField()
    phone_number = models.CharField(max_length=20)
    aadhar_number = models.CharField(max_length=12)
    policy_id = models.CharField(max_length=12)
    is_valid_policy_id = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    location = models.CharField(max_length=20)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    designation = models.CharField(max_length=20)

class Appointment(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    aadhar=models.CharField(max_length=12)
    policy=models.CharField(max_length=12)
    coupon=models.CharField(max_length=10)
    appointment_date=models.DateField()
    department=models.CharField(max_length=50)
    doctor=models.CharField(max_length=50)
    message=models.CharField(max_length=100)
    symptoms=models.CharField(max_length=100)

