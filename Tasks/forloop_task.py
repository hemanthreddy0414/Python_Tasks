#Find the average of numbers from 1 to N.
# n=5                             
# sum=0
# for i in range(1,n+1,1):
#     sum=(n*(n+1)/2)
#     avg=sum//n
# print("sum : ",sum)
# print("avg : ",avg)


#Find the sum of squares of numbers from 1 to N.
# n=5                                          
# for i in range(1,n+1,1):
#         print(i**2)


# n=5                                          #squares with sum
# sum=0
# for i in range(1,n+1,1):
#     if(i**2):
#         print(i," = ",i**2)
#         sum=sum+i**2
# print("sum of squares = ",sum)



#Find the sum of cubes of numbers from 1 to N.
# n=5                                           #cubes
# for i in range(1,n+1,1):
#         print(i**3)
    

# n=5                                    
# sum=0
# for i in range(1,n+1,1):
#     if(i**i):
#         print(i," = ",i**3)
#         sum=sum+i**3
# print("sum of cubes = ",sum)



#Calculate the power of a number without using the ** operator.
# n=2                                     #powers of 2
# for i in range(1,6):
#     print(pow(n,i))

# n=2                                     #sum of 2 powers
# sum=0
# for i in range(1,6):
#     sum=sum+(pow(n,i))
# print(sum)
        

#Display the first N terms of the Fibonacci series.
# n=int(input("Enter Number :"))
# a=0
# b=1
# for i in range(1,n+1,1):
#     print(a)
#     c=a+b
#     a=b
#     b=c


#Display the first N terms of the series:
    # 1, 11, 111, 1111, 11111, ...
# n=int(input("Enter Number : "))
# num=0
# for i in range(0,n+1,1):
#     num=num*10+1
#     print(num)


#Display the first N terms of the series:
# n=int(input("Enter Number : "))
# print("1")
# for i in range(2,n+1,1):
#     print(1,"/",i)
    

# display the first N terms of the series
# n=3                                    
# for i in range(0,5):
#     print(3**i)
    

# for j in range(1,500,1):                   #armstrong numbers
#     n=j
#     sum=0
#     new=n
#     digit=0
#     while n>0:
#         ld=n%10
#         digit=ld**3
#         sum=sum+digit
#         n=n//10
#     if sum==new:
#         print("armstrong",j)