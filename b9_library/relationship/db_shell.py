
# exec(open(r"D:\code_files\DjangoProjects\b9_library\relationship\db_shell.py").read())

from datetime import date
from relationship.models import *

# Person.objects.create(name="BBB", age= 26,  mobail =7233221133, email = "bbb@gmil.com")
# Person.objects.create(name="ccc", age= 27,  mobail =980809909, email = "ccc@gmil.com")
# Person.objects.create(name="ddd", age= 28,  mobail =7633244322, email = "ddd@gmil.com")

# all = Person.objects.all()
# for i in all:
#     print(i)


# p3 = Person.objects.get(id= 3)
# print(p1)
# first way
# Aadhar.objects.create(aadhar_number=387390622612,address = "pal", BOD =date(1999,7, 25),  Person = p1)

# Aadhar.objects.create(aadhar_number=554466332222,address = "phulambri", BOD =date(1998,8, 24),   Person=p1 )


# 2 way
# Aadhar.objects.create(aadhar_number=9988776655,address = "pal", BOD =date(1999,4, 2), Person_id  =2 )

# p3 = Person.objects.get(id= 3)
# a1 = Aadhar(aadhar_number=884433344,address = "sambhajinagar", BOD =date(1988,4, 3) )
# a1.save()

# 3rd way

# a3 = Aadhar.objects.get(id = 1)
# print(a3)
# a3.Person = p3
# a3.save()


# aadhar se person fetch kiya
# a3 = Aadhar.objects.get(id = 2)
# print(a3.Person.name)
# print(a3.Person.age)
# print(a3.Person)
# print(a3.address)

# person se Aadhar
# p1 = Person.objects.get(id =1)
# print(p1.aadhar.address)
# print(p1.aadhar.__dict__)
# print(p1.__dict__)




# select_related
# Aadhar.objects.all().select_related("person")

# for i in Aadhar.objects.all().select_related("person"):
#     print(i.Person)
#     print(i.aadhar_number)


# for p in Person.objects.all().select_related("adhar_number"):
#     print(p)
    
# exec(open(r"D:\code_files\DjangoProjects\b9_library\relationship\db_shell.py").read())



# one two many

# from relationship.models import Car, CarModel

# mercedes = Car.objects.create(name = "Mercedes")
# bmw = Car.objects.create(name = "BMW")

# data =Car.objects.all()
# print(data)

# mercedes = Car.objects.get(name = "Mercedes")
# c180 = CarModel.objects.create(name = "c180", car = mercedes)
# c180 = CarModel.objects.get(name="c180")
# # print(c180.car)
# print(c180.__dict__)

# car se CarModel fetch recorde

# c1 =  Car.objects.get(name  = "Mercedes")
# print(c1.CarModel_set.all())

# c200 = CarModel.objects.create(name= "c200")
# c200.save()

# c200 = CarModel.objects.get(name= "c200")
# print(c200.car.name)




# x1 = CarModel.objects.create(name = "x1")
# x2 = CarModel.objects.create(name = "x2")

# for car_model in CarModel.objects.all():
#     print(car_model)


# bmw = Car.objects.get(name="BMW")
# bmw.carmodel.add(x1, x2)


# model = CarModel.objects.filter(car__name = "Mercedes")
# print(model)

# model = CarModel.objects.filter(car__name__startwith = "M")
# print(model)




# mony to mony relationship

# c180 = CModel.objects.create(name ="c180")    #CModel me value add honar c180 and c200
# c200 = CModel.objects.create(name ="c1200")


# gas = FuelType.objects.create(name = "Gas")
# disel = FuelType.objects.create(name = "Diesel")
# hybrid = FuelType.objects.create(name = "Hybrid")

# c180 = CModel.objects.get(name = "c180")
# print(c180)
# print(c180.fueltype.all())

# gas = FuelType.objects.get(name= "Gas")
# print(gas)

# diesel = FuelType.objects.get(name = "Diesel")
# c180.fueltype.add(diesel)

print("""relation ship type
one to one
one to many
and many to many""")

# exec(open(r"D:\code_files\DjangoProjects\b9_library\relationship\db_shell.py").read())

print("in f1 branch")


