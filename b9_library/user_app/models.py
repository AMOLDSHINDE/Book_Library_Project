from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length= 100)
    age = models.IntegerField()
    email = models.EmailField()
    mobail = models.BigIntegerField(null= True, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "person"







class Aadhar(models.Model):
    aadhar_number = models.BigIntegerField(unique=True)
    address = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now= True)
    Person = models.OneToOneField(Person, on_delete= models.CASCADE)
    BOD = models.DateField()



    class Meta:
        db_table ="aadhar"