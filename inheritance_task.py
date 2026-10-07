#single inheritance without constructor

# class Company:
#     def comname(self):
#         print("company name")

# class Product(Company):
#     def pname(self):
#         print("product name")

# p=Product()
# p.comname()
# p.pname()


# single inheritance with constructor

# class Vehicle:
#     def __init__(self,Brand,price):
#         self.Brand = Brand
#         self.price = price

#     def data(self):
#         print("Car brand : ",self.Brand)
#         print("Car price : ",self.price)

# class Car(Vehicle):
#     def __init__(self,Brand,price,model,cc):
#         self.Brand = Brand
#         self.price = price
#         self.model = model
#         self.cc = cc

#     def details(self):
#         print("car brand : ",self.Brand)
#         print("car price : ",self.price)
#         print("car model : ",self.model)
#         print("car cc : ",self.cc)

# c=Car("KIA",500000,"SELTOS",1350)
# c.details()
    

#single inheritance with constructor and super+

# class College:
#     def __init__(self,name,course):
#         self.name = name
#         self.course = course

#     def data(self):
#         print("Name of Student : ",self.name)
#         print("Course Name : ",self.course)

# class Student(College):
#     def __init__(self,name,course,age,year):
#         super().__init__(name,course)
#         self.age = age
#         self.year = year

#     def details(self):
#         super().data()
#         print("Age of student : ",self.age)
#         print("year of student : ",self.year)

# s=Student("akhil","CSM",21,2026)
# s.details()



# single inheritance using constructor with super and real word example
# class Bank:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Account(Bank):
#     def __init__(self,name,age,acc_type,balance):
#         super().__init__(name,age)
#         self.acc_type = acc_type
#         self.balance = balance

#     def data(self):
#         print("Account holder name : ",self.name)
#         print("Age : ",self.age)
#         print("Account type : ",self.acc_type)
#         print("Available Balance : ",self.balance)

# A=Account("akhil",21,"savings",25000)
# A.data()

# ----------------------------------------------------------Multilevel inheritance
# multilevel inheritance without constructor

# class Gp:
#     def m1(self):
#         print("Grand parent assets")

# class P(Gp):
#     def m2(self):
#         print("Parent assets")

# class C(P):
#     def m3(self):
#         print("child assets")

# c=C()
# c.m1()
# c.m2()
# c.m3()


# multilevel with constructor
# class Company:
#     def __init__(self,c_name,location):
#         self.c_name = c_name
#         self.loction = location

# class Employee(Company):
#     def __init__(self,c_name,location,Emp_name,Emp_age):
#         self.c_name = c_name
#         self.location = location
#         self.Emp_name = Emp_name
#         self.Emp_age = Emp_age

# class Developer(Employee):
#     def __init__(self,c_name,location,Emp_name,Emp_age,Dev_Domain,Dev_salary):
#         self.c_name = c_name
#         self.location = location
#         self.Emp_name = Emp_name
#         self.Emp_age = Emp_age
#         self.Dev_Domain = Dev_Domain
#         self.Dev_salary = Dev_salary

#     def data(self):
#         print("Company name : ",self.c_name)
#         print("Company Location : ",self.location)
#         print("Employe Name : ",self.Emp_name)
#         print("Employe age : ",self.Emp_age)
#         print("Developer Domain : ",self.Dev_Domain)
#         print("Developer salary : ",self.Dev_salary)

# D=Developer("Deloitte","HYD","Akhil",21,"Python",25000)
# D.data()


# mulitilevel inheritance with constructor and super
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

# class Manager(Employee):
#     def __init__(self,name,salary,role):
#         super().__init__(name,salary)
#         self.role = role

#     def details(self):
#         print("Employee name : ",self.name)
#         print("Employee salary : ",self.salary)
#         print("role : ",self.role)

# M=Manager("akhil",25000,"Developer")
# M.details()



# class Vehicle:
#     def __init__(self,Brand,model,price):
#         self.Brand = Brand
#         self.model = model
#         self.price = price

# class Car(Vehicle):
#     def __init__(self,Brand,model,price,car_type):
#         super().__init__(Brand,model,price)
#         self.car_type = car_type

# class Sportscar(Car):
#     def __init__(self,Brand,model,price,car_type,variant):
#         super().__init__(Brand,model,price,car_type)
#         self.variant = variant

#     def details(self):
#         print("Car Brand : ",self.Brand)
#         print("Car Model : ",self.model)
#         print("Car price : ",self.price)
#         print("Car motor type : ",self.car_type)
#         print("Car variant : ",self.variant)

# s=Sportscar("Maruthi","Breeza",550000,"Ev","Top variant")
# s.details()