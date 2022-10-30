from django.contrib import admin
from .models import Appointment, User, Customer, Employee

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Appointment)