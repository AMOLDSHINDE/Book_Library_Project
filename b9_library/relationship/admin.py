
from django.contrib import admin

# Register your models here.
from relationship.models import *

admin.site.register([Person, Aadhar])   #, Car,  CarModel,FuelType, CModel

print("hi hello in master")