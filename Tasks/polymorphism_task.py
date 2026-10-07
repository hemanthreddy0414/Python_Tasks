#polymorphism using single inheritance

# class A:
#     def single(self):
#         print("single method from A")

# class B(A):
#     def single(self):
#         print("single method from B")

# b=B()
# b.single()
# print(B.mro())

# a=A()
# a.single()
# print(A.mro())


# class Vehicle:
#     def move(self):
#         print("Vehicle Ready to Race")

# class Car(Vehicle):
#     def move(self):
#         print("Car Ready to Race")

# c=Car()
# c.move()

# v=Vehicle()
# v.move()


#-------------------------------------------------------------
#multilevel inheritance
# class A:
#     def m1(self):
#         print("m1 from A")

# class B(A):
#     def m1(self):
#         print("m1 from B")

# class C(B):
#     def m1(self):
#         print("m1 from C")

# c=C()
# c.m1()
# print(C.mro())

# b=B()
# b.m1()
# print(B.mro())

# a=A()
# a.m1()
# print(A.mro())


# class Person:
#     def salary(self):
#         print("salary from Person")

# class Employee:
#     def salary(self):
#         print("salary from Employee")

# class Manager:
#     def salary(self):
#         print("salary from Manager")

# m=Manager()
# m.salary()
# print(Manager.mro())


# e=Employee()
# e.salary()
# print(Employee.mro())


# p=Person()
# p.salary()
# print(Person.mro())


#----------------------------------------------------------
#Hierarichal inheritance

# class A:
#     def m1(self):
#         print("m1 from A")

# class B(A):
#     def m1(self):
#         print("m1 from B")

# class C(A):
#     def m1(self):
#         print("m1 from C")

# a=A()
# a.m1()
# print(A.mro())


# b=B()
# b.m1()
# print(B.mro())

# c=C()
# c.m1()
# print(C.mro())



#------------------------------------------------------------------------------------------
#multiple inheritance

# class A:
#     def m1(self):
#         print("M1 fom A")

# class B:
#     def m1(self):
#         print("m1 from B")

# class C(A,B):
#     def m1(self):
#         print("m1 from C")

# c=C()
# c.m1()
# print(C.mro())



#-------------------------------------------------------------------------
#Hybrid inheritance

# class A:
#     def m1(self):
#         print("m1 from A")

# class B(A):
#     def m1(self):
#         print("m1 from B")

# class C(A):
#     def m1(self):
#         print("m1 from C")

# class D(B,C):
#     def m1(self):
#         print("m1 from D")

# d=D()
# d.m1()
# print(D.mro())