# Restaurant Menu


# print("Restaurant Menu")
# print("1.Biryani")
# print("2.Chicken 65")
# print("3.Veg pulao")
# print("4.Butter Chicken")
# print("5.Panner Tikka")
# select=int(input("enter value : "))

# match select:
#     case 1:
#         print("item :Biryani")
#         print("price : 250")
#         print("Description :  Crispy and spicy deep-fried chicken pieces.")
#     case 2:
#         print("item :Chicken 65")
#         print("price : 300")
#         print("Description :  Crispy and spicy deep-fried chicken pieces.")
#     case 3:
#         print("item :Veg pulao")
#         print("price : 249")
#         print("Description :  Crispy and spicy deep-fried chicken pieces.")
#     case 4:
#         print("item :Butter Chicken")
#         print("price : 299")
#         print("Description :  Crispy and spicy deep-fried chicken pieces.")
#     case 5:
#         print("item :Panner Tikka")
#         print("price : 499")
#         print("Description :  Crispy and spicy deep-fried chicken pieces.")
#     case _:
#         print("currently unavailable")




# -------------------------------------------------------------------------

# ATM Menu using match case

# print("ATM Menu")
# print("1.Check Balance")
# print("2.Deposit")
# print("3.Withdraw")
# print("4.Exit")
# n1=10000
# select=int(input("enter your choice :"))

# match select:
#     case 1:
#         print("Current Balance :",n1)
#     case 2:
#         n2=int(input("Enter Deposite Amount :"))
#         print(n1 + n2)
#         print("Deposited Successfully")
#     case 3:
#         n3=int(input("Enter Withdraw Amount :"))
#         print(n1 - n3)
#         print("Withdraw Successfully")
#         print("Remaining amount :",n1 - n3)
#     case 4:
#         print("Thank you for using ATM")
#     case _:
#         print("invalid credential")



#-----------------------------------------

# Electricity Bill Calculator

# unit=int(input("Enter Units :"))

# if (unit>=0) and (unit<=100):
#     print("Total Bill :",unit*2)
# elif (unit>=101) and (unit<=200):
#     print("Total Bill :",unit*4)
# elif (unit>=201) and (unit<=300):
#     print("Total Bill :",unit*6)
# elif  (unit>=300):
#     print("Total Bill :",unit*8)
# else:
#     print("Invalid units")



#-------------------------------------------------

# Write a Python program to check whether the given year is a leap year or not.

# year=int(input("Enter Year : "))

# if (year%400==0) or (year%4==0):
#     print("Leap year")
# else:
#     print("Not leap year")