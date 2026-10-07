# ----------------------------functions task with various logics-----------------------------------
# functions without input and without return
# Check whether a number is positive, negative, or zero.
# def number():
#     n=int(input("Enter a number :"))
#     if n>=0:
#         print("Positive")
#     else:
#         print("Negative")
# number()



# For Loop – Print all even numbers from 1 to 50.
# def even():
#     for i in range(1,50):
#         if i%2==0:
#             print(i,"even")
# even()



# While Loop – Reverse a given number.
# def reverse():
#     n=int(input("Enter a number :"))
#     while n>0:
#         ld=n%10
#         n=n//10
#         print(ld)
# reverse()


# odd numbers 1 to 20
# def odd():
#     for i in range(1,21):
#         if i%2!=0:
#             print(i,"odd")
# odd()


#prime numbers 1 to 10
# def prime():
#     n=int(input("Enter number :"))
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count=count+1
#     if count==2:
#         print(n,"is prime number")
#     else:
#         print(n,"is not prime number")
# prime()
        

#factors
# def factors():
#     n=int(input("Enter number :"))
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i)
# factors()


# factorials
# def fact():
#     n=5
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# fact()

# perfect number
# def perfect():
#     for j in range(1,10000,1):
#         n=j
#         sum=0
#         for i in range(1,n):
#             if n%i==0:
#                 sum=sum+i
#         if sum==n:
#             print(sum,"is perfect number")
# perfect()


# palindrome or not
# def palindrome():
#     for j in range(11,1000):
#         n=j
#         rev=0
#         new=n
#         while n>0:
#             ld=n%10
#             rev=rev*10+ld
#             n=n//10
#         if rev==new:
#             print(rev,"is palindrome")
# palindrome()