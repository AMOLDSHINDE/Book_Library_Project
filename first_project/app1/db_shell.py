from app1.models import Student

# exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())

# all_studs = Student.objects.all()
# print(all_studs)
# all_studs = Student.objects.all()
# print(all_studs.query)
# print(list(all_studs))

# all_studs = Student.objects.all()[0]
# print(all_studs)

# all_studs = Student.objects.all()
# print(all_studs.__dict__)
# for i in all_studs:
#     print(i)

# for i in all_studs:
#     print(f"------------------stud id:-{i.id}---------------------")
#     print(i.show_details())

# 2nd way
# s2 = Student(name = "bhart", address = "babara", age =35, salary =70000)
# s2.save()


# 1st way
# Student.objects.create(name = "sham", address = "vadi", age =40, salary =80000)    #object create bhi krlage or save bhi karlega

# s1 = Student(name = "abc", address = "address1", age =35, salary =40000)
# s2 = Student(name = "def", address = "address2", age =30, salary =30000)
# s3 = Student(name = "ghi", address = "address3", age =25, salary =45000)

# Student.objects.bulk_create([s1,s2, s3])




# Stud_obj = Student.objects.get(address = "address3")
# print(Stud_obj)



# Stud_obj = Student.objects.get(name = "AMOL")
# print(Stud_obj)

# try:
#     stud_obj = Student.objects.get(name = "ram")
# except Student.MultipleObjectsReturned:
#     print("more than  1 recode found")


# stud_obj = Student.objects.filter(name = "ram")  #filter se 1 hi name ke 2 log hoge to donokebhi record milege

# print(stud_obj)


# stud = Student.objects.get(id = 10)
# stud.name = "ccccc"
# stud.age = 34
# stud.save()
# print(stud)

# Student.objects.all().delete()
# Student.objects.filter(address = "pal").delete()



# Django ORM  Queries============================================
# exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# exec la comment karaych ani terminak la exec(open(r"").read()) past kraych nahi kelatr requrism error

# print(Student.objects.count())     #kiti data ahet te count krun denar


# record = Student.objects.filter(name__startswith ="A" )
# print(record)

# record = Student.objects.filter(name__endswith ="l" )
# print(record)

# record= Student.objects.filter(name__in = ["AMOL", "amol", "A"])
# print(record)

# print(Student.objects.exclude(address = "pal"))

# print(len(Student.objects.exclude(address = "pal")))

# first way of or operers
# res =Student.objects.filter(name__startswith = "A") | Student.objects.filter(address__endswith = "l")
# print(res)



# res = Student.objects.filter(name = "ajay", address = "pal")
# print(res)

# print(Student.objects.filter(name__contains = "a"))       #jya madhe a ahet te all print honar

# from django.db.models import Q, F
# res = Student.objects.filter(Q(name__startswith = "A") | Q(address__startswith = "p"))
# print(res)


# res = Student.objects.filter(Q(name__startswith = "A")&Q(address ="pal")&Q(salary =45000))
# print(res)

# data = Student.objects.filter( Q(age__gt= 25)& Q(salary__lt = 45000))
# print(data)

# data = Student.objects.filter( Q(age__gte= 25)& Q(salary__lt = 45000))
# print(data)

# Student.objects.all().update(salary =F('salary')+ 5000)   #sabki salary 5000 thousond se badegi

# Student.objects.filter(name = "Amol").update(name = "amol")

# print(Student.objects.all().order_by("name"))   #asending order madhe bhetanar daata terminal maghe


# print(Student.objects.all().order_by("-name"))    #- minus sine lavly varti desending order madhe data bhetnar tarminl madhe



# from django.db.models import Avg, Sum,Min, Max
# print(Student.objects.all().aggregate(Avg("salary")))


# Student.objects.all().delete()  #ise sararecord delete ho jayega

# a = Student.objects.filter(id__lt  = 4)
# b = Student.objects.filter(salary__gt = 45000)
# res =a.union(b)
# print(res)


# xlsx file cha data mysql madhe add honar
# import openpyxl

# wb = openpyxl.load_workbook(r"D:\code_files\xyz.xlsx")
# sheet = wb.active

# print(sheet.max_row)

# lst = []
# for i in range(2, sheet.max_row + 1):  # 8
#     nm = sheet.cell(row=i, column=1).value
#     adr = sheet.cell(row=i, column=2).value
#     ag = sheet.cell(row=i, column=3).value
#     sala = sheet.cell(row=i, column=4).value
#     # obj = Student(name=nm,  address=adr, age=ag, salary = sala)
#     # if salary >= 10000:
#     if sala >= 50000:
#         obj = Student(name=nm, address=adr, age=ag, salary = sala)
#         lst.append(obj)

#     lst.append(obj)

# Student.objects.bulk_create(lst)

# # to run row sql queries using jango
# data = Student.objects.raw("select * from Student")   #consol madhe disnar all data
# for i in data:
#     print(i)


# from django.db import connection

# curser = connection.cursor()
# curser.execute("select * from Student where name = 'A'")
# data = curser.fetchall()
# print(data)



# excel --file data-- read and write to db using django












# first_progect
    # first_project   --- directory
#      - settings.py
#      - asgi.py
#      - wsgi.py
#      -- urls.py
#     manage.py  =-- to interact with ur progect --
#     app
#       migrations ---director   ---migrated file hoti he
#       --init__.py
#     admin,py        -----------admin ki activeti krnekeliye
#     models.py          ------ jahape table criate krte he
#     app.py                 ---aap ka configration hota he
#     test.py 
#     __init__.py
#     views.py ----buseness logic

# __init__.py  python packege-- import--


# models.py ---OMR---object relation MApping

# pip install virtualenv                               #INVEERMENT Banavnya sati virtualenv install kraval lageto ani 

# virtualenv b9_env

# cd \Scripts\

# activate

# deactivate.bat

# activate




# django to db_broser=========================================================


# D:\code_files>mkdir DjangoProjects

# D:\code_files>cd DjangoProjects

# D:\code_files\DjangoProjects>django-admin startproject first_project


# (b9_env) D:\code_files\DjangoProgect\first_progect>python manage.py startapp app1          #project madhe app banvnysati hi qurry hit kravi lagte
# 1st go to setting
# install_Apps me - app1 -manualy app tayar kiya he o oh dalneka

# 2nd go to models.py
# class Student(models.Model):
#   #  sid - models.intgerField  #django atomatical id leleta he   
#     name = models.CharField(maz_lenth =100)
#     marks = models.IntegerField()
#     address = models.CharField(max_lenth = 100)

# (b9_env) D:\code_files\DjangoProgect\first_progect>python manage.py makemigrations  #bakend mesql qurey genaret hogi

# app1 me 0001 ki file banegi

# (b9_env) D:\code_files\DjangoProgect\first_progect>python manage.py sqlmigrate app1 0001

# (b9_env) D:\code_files\DjangoProgect\first_progect>python manage.py migrate   #ese data add hoga db brosser me


# 3rd admin.py ----me likhneka ---
  #     from .models import Student
      # admin.site.register([Student])
# (b9_env) D:\code_files\DjangoProgect\first_progect>python manage.py createsuperuser 
   #DATA BHARAYCH 

# (b9_env) D:\code_files\DjangoProgect\first_progect>python manage.py runserver


# 4th urls.py
# (b9_env) D:\code_files\DjangoProgect\first_progect>py manage.py runserver

# seach me 127.0.01..8000
# seach me 127.0.01..8000/admin/
# #(b9_env) D:\code_files\DjangoProgect\first_progect>python manage.py runserver 4444 (new server tayar karsate he )

# 5th models.py
# def __str__(self):
#     return f"{self.name}"        #name address, age  id jo chiye o dalneka


# time o change krna he to setting me kr saktehe

# (b9_env) D:\code_files\DjangoProgect\first_progect>py manage.py changepassword Amol     #jiskeliye change krnahe uska name dalne ka


# file share kraychi asel tr 
# pip freeze  > requrement.txt

# (b9_env) D:\code_files>dir > req.txt

# (b9_env) D:\code_files>cd DjangoProgect

# (b9_env) D:\code_files\DjangoProgect>cd first_progect

# (b9_env) D:\code_files\DjangoProgect\first_progect>python manage.py startapp app1

# (b9_env) D:\code_files\DjangoProgect\first_progect>python manage.py makemigrations

# (b9_env) D:\code_files\DjangoProgect\first_progect>python manage.py sqlmigrate app1 0001

# (b9_env) D:\code_files\DjangoProgect\first_progect>python manage.py createsuperuser  

# (b9_env) D:\code_files\DjangoProgect\first_progect>python manage.py runserver















# the mvt (model view template) is a software design pattern

# model: model is going to act as the interface of data 
# view : the view is the user interface -- what you see  in your browser when  reader you reader a website
# template: a template consist of static parts of the desired HTML output as some special Syntax 
# describing how dynamic content willbe inserted

# views:-the logic is executed for diffrent URLs---used --funtion and classs
    
        

# mysql data add krna he django se add phi krenge or terminal me read bhi krlege===========================================
# go to setting and change database:

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'b9_student',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
    
# }

# go to model : model madhe gely natr define the class
# class classname(model.Model):
#     id= id djago atomatic le leta he esme id define krneki jarurat nahi hoti
#     name=model.charFild(max_lenth = 100)
#     address=---
#     age=  model.integerFilde()

# after go to mysql: and creat database
# use DATABASES name


# go to admin: import models file and give database name
# admin.site.register([Student]) hi commod ghyvich lagel


# from .models import Student
# admin.site.register([Student])

# go to model jr db_table name jr change kraych asel tr  Meta class define krach  nested class asto To 
#  class Meta:
#     db_table = "chage name "

# >> from app1.models import Student
# >>> Student
# <class 'app1.models.Student'>
# >>> Student.objects.all()
# <QuerySet []>
# >>> list(Student.objects.all())
# []
# 25, salary=45000)                                    25, salary=45000)
# >>> s1
# <Student: AMOL>
# >>> s1.save()

# s1 = Student(name = "amol", address = "pal", age = 25)



# make db_shall.py file and create operation and path leneka and terminal me pest krne ka
# db_shall.py me from app1.models import Student


# exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())

# all_studs = Student.objects.all()
# print(all_studs)



#                                    de object        
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_sheoject\app1\db_shell.py").read())
# <QuerySet [<Student: AMOL>]>
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# >>>
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# <QuerySet [<Student: AMOL>, <Student: abc>, <Student: puja>, <Student: ajay>, <Student: bhart>, <Student: ram>, <Student: ram>, <Student: sham>, <Student: abc>, <Student: def>, <Student: ghi>]>
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# SELECT `student`.`id`, `student`.`name`, `student`.`address`, `student`.`age`, `student`.`salary` FROM `student`
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# [<Student: AMOL>, <Student: abc>, <Student: puja>, <Student: ajay>, <Student: bhart>, <Student: ram>, <Student: ram>, <Student: sham>, <Student: abc>, <Student: def>, <Student: ghi>]
# >>>  exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
#   File "<console>", line 1
#     exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# IndentationError: unexpected indent
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# AMOL
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# {'_state': <django.db.models.base.ModelState object at 0x000002797120C5D0>, 'id': 1, 'name': 'AMOL', 'address': 'pal', 'age': 25, 'salary': 45000}        
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# {'model': <class 'app1.models.Student'>, '_db': None, '_hints': {}, '_query': <django.db.models.sql.query.Query object at 0x00000279711DCDD0>, '_result_cache': None, '_sticky_filter': False, '_for_write': False, '_prefetch_related_lookups': (), '_prefetch_done': False, '_known_related_objects': {}, '_iterable_class': <class 'django.db.models.query.ModelIterable'>, '_fields': None, '_defer_next_filter': False, '_deferred_filter': None}
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# {'model': <class 'app1.models.Student'>, '_db': None, '_hints': {}, '_query': <django.db.models.sql.query.Query object at 0x000002797120CC90>, '_result_cache': None, '_sticky_filter': False, '_for_write': False, '_prefetch_related_lookups': (), '_prefetch_done': False, '_known_related_objects': {}, '_iterable_class': <class 'django.db.models.query.ModelIterable'>, '_fields': None, '_defer_next_filter': False, '_deferred_filter': None}
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# {'_state': <django.db.models.base.ModelState object at 0x000002797120C6D0>, 'id': 3, 'name': 'puja', 'address': 'nagpur', 'age': 26, 'salary': 55000}     
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())

# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# AMOL
# abc
# puja
# ajay
# bhart
# ram
# ram
# sham
# abc
# def
# ghi
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# ------------------stud id:-1---------------------
# NAME : AMOL
# address:- pal
# age:-25
# salary:-45000

# ------------------stud id:-2---------------------
# NAME : abc
# address:- pathri
# age:-25
# salary:-50000

# ------------------stud id:-3---------------------
# NAME : puja
# address:- nagpur
# age:-26
# salary:-55000

# ------------------stud id:-4---------------------
# NAME : ajay
# address:- pal
# age:-24
# salary:-60000

# ------------------stud id:-5---------------------
# NAME : bhart
# address:- babara
# age:-35
# salary:-70000

# ------------------stud id:-6---------------------
# NAME : ram
# address:- vadi
# age:-40
# salary:-80000

# ------------------stud id:-7---------------------
# NAME : ram
# address:- vadi
# age:-40
# salary:-80000

# ------------------stud id:-8---------------------
# NAME : sham
# address:- vadi
# age:-40
# salary:-80000

# ------------------stud id:-9---------------------
# NAME : abc
# address:- address1
# age:-35
# salary:-40000

# ------------------stud id:-10---------------------
# NAME : def
# address:- address2
# age:-30
# salary:-30000

# ------------------stud id:-11---------------------
# NAME : ghi
# address:- address3
# age:-25
# salary:-45000


# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# abc
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# ghi
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# AMOL
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# <QuerySet [<Student: ram>, <Student: ram>]>
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# def
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# def
# >>> exec(open(r"D:\code_files\DjangoProjects\first_project\app1\db_shell.py").read())
# >>>