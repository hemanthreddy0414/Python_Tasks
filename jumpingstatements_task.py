# Find the first even digit from the left in 753914286.
# n=753914286
# while n>0:
#     ld=n%10
#     if ld==4:
#         break
#     n=n//10
#     print(ld)



# Find the first prime number between 50 and 100.
# for j in range(50,101,1):
#     n=j
#     count=0
#     for i in range(1,n+1,1):
#         if n%i==0:
#             count=count+1
#     if count==2:
#         print(n,"is prime number")
   


# Find the first perfect number between 1 and 1000.
# for j in range(1,1001,1):
#     n=j
#     sum=0
#     for i in range(1,n,1):
#         if n%i==0:
#             sum=sum+i
#     if sum==n:
#         print(n,"perfect number")



# Find the first palindrome between 10 and 500.
# for j in range(10,501,1):
#     n=j
#     rev=0
#     new=n
#     while n>0:
#         ld=n%10
#         n=n//10
#         rev=rev*10+ld
#     if rev==new:
#         print(rev,"is palindrome")


# Print the first 5 even numbers.
# count=0
# for i in range(1,20,1):
#     if i%2==0:
#         print(i)
#         count=count+1
#         if count==5:
#             break
        

# Print the first 5 prime numbers.
# totalcount=0
# for j in range(1,21,1):
#     n=j
#     count=0
#     for i in range(1,n+1,1):
#         if n%i==0:
#             count=count+1
#     if count==2:
#        print(n)
#        totalcount=totalcount+1
       
#     if totalcount==5:
#         break
    
        
# Print the first 3 numbers divisible by 7
# count=0
# for i in range(1,70,1):
#     if i%7==0:
#         count=count+1
#         print(i)
#         if count==3:
#             break


# Stop when 3 consecutive odd numbers occur between 1 and 50.
# count=0
# for i in range(1,51,1):
#         if i%2!=0:
#             count=count+1
#             print(i)
#             if count==3:
#                 break