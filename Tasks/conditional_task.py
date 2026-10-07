#check whether a given number is 3 digit number or not
# n=int(input("Enter number : "))
# if(n>99) and (n<1000):
#     print("given number is 3 digit")
# else:
#     print("given number is not 3 digit")


#check whether a given number is divisible by both 3 and 5 or not
# n=int(input("Enter number : "))
# if (n%3==0) and (n%5==0):
#     print(n,"is divisible by 3 & 5")
# else:
#     print(n,"is not divisible by 3 & 5")

# check whether a given triangle is valid triangle or not
# a=int(input("side 1 :"))
# b=int(input("side 2 :"))
# c=int(input("side 3 :"))
# if a+b>c or b+c>a or c+a>b:
#     print("valid")
# else:
#     print("invalid")


#check given number is multiple of 10 or not
# n=int(input("Enter number : "))
# if (n%10==0):
#     print(n,"is divisible by 10")
# else:
#     print(n,"is not divisible by 10")


#if elif else-----------------------

#check the type of triangle based on its side
# a=int(input("Enter number : "))
# b=int(input("Enter number : "))
# c=int(input("Enter number : "))
# if (a==b) and (b==c):
#     print("Equilateral triangle")
# elif (a==b) and (b!=c):
#     print("Isosceles")
# elif (a!=b) and (b!=c):
#     print("Scalene")
# else:
#     print("invalid triangle")


#Calculate the electricity bill based on units consumed.
    # 0–100: ₹2/unit, 101–200: ₹3/unit, 201–300: ₹5/unit, above 300: ₹7/unit.
# n=int(input("Enter number : "))
# if (n>=0) and (n<=100):
#     print("units below 100 total bill : ",n*2)
# elif(n>=101) and (n<=200):
#     print("units below 200 total bill : ",n*3)
# elif(n>=201) and (n<=300):
#     print("units below 300 total bill : ",n*5)
# elif(n>300):
#     print("units above 300 total bill : ",n*7)
# else:
#     ("Invalid unit")


#.Display the age category.
    # Below 13 → Child, 13–19 → Teenager, 20–59 → Adult, 60 and above → Senior Citizen.
# n=int(input("Enter number : "))
# if (n<13):
#     print("child")
# elif (n>=13) and (n<=19):
#     print("Teenager")
# elif (n>=20) and (n<=59):
#     print("Adult")
# elif (n>=60):
#     print("Senior Citizen")
# else:
#     print("invalid age")



#Display the season based on the month number.
# n=int(input("Enter number : "))
# if(n>=3) and (n<=5):
#     print("spring")
# elif (n>=6) and (n<=8):
#     print("summer")
# elif (n>=9) and (n<=11):
#     print("Autumn")
# elif (n==1) or (n==2) or (n==12):
#     print("Winter")
# else:
#     print("Invalid number")


#Check whether a given year is a Leap Year or not.
# n=int(input("Enter number : "))
# if (n%400==0) or (n%4==0) and (n%100!=0):
#     print(n,"leap year")
# else:
#     print(n,"is not leap year")



#Check whether a person is eligible to donate blood.
    # Age should be between 18 and 60. If eligible by age, weight should be above 50 kg.
# age=int(input("Enter Age : "))
# w=int(input("Enter Weight : "))
# if (age>=18) and (age<=60):
#     print(age,"eligible to vote") 
#     if(w>50):
#         print(w,"weight is above 50")
#     else:
#         print(w,"weight is below 50")
# else:
#     print(age,"not eligible to vote")


#Check whether a student is eligible for a scholarship.
    # Age should be above 18. If eligible by age, score should be above 86.

# age=int(input("Enter Age : "))
# score=int(input("Enter Score : "))
# if (age>=18):
#     print("eligible to scholarship")
#     if (score>=86):
#         print("score is eligible to scholarship")
#     else:
#         print("score is not eligible to scholarship")
# else:
#     print("not eligible to scholarship")


#Display the grade based on average only if the student has passed in all 4 subjects.
# sub1=int(input("Enter sub1 marks : "))
# sub2=int(input("Enter sub2 marks : "))
# sub3=int(input("Enter sub3 marks : "))
# sub4=int(input("Enter sub4 marks : "))
# if sub1>=35 and sub2>=35 and sub3>=35 and sub4>=35:
#     total=sub1+sub2+sub3+sub4
#     avg=total//4
#     print("pass")
#     if avg>90:
#         print("Grade O")
#     elif avg>71 and avg<90:
#         print("Grade A")
#     elif avg>50 and avg<70:
#         print("Grade B")
#     elif avg>=35 and avg<50:
#         print("Grade c")
#     else:
#         print("Grade E")
# else:
#     print("fail")


#Calculate the discount based on shopping amount.
# Below ₹1,000 → No discount, ₹1,000–₹4,999 → 10%,₹5,000–₹9,999 →20%,₹10,000 and above →30%.

# shop=int(input("Enter shopping amount : "))
# if shop<1000:
#     print("No Discount")
# elif shop>=1000 and shop<=4999:
#         discount=shop*10/100
#         print(discount,"applied discount")
# elif shop>=5000 and shop<=9999:
#         shop*20/100
#         discount=shop*20/100
#         print(discount,"applied discount")
# elif shop>10000:
#         shop*30/100
#         discount=shop*30/100
#         print(discount,"applied discount")
# else:
#     print("Shop above 1k you will get discount")