from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null= True)
    salary = models.IntegerField(null= True)

    def __str__(self):
        return f"{self.__dict__}"
        # return f"{self.name}"
    
    def show_details(self):
        return f"""NAME : {self.name}
address:- {self.address}
age:-{self.age}
salary:-{self.salary}
"""

    class Meta:   #nested class
        db_table = "student"
