#1.Find the sum of digits in a given number.
    # Example: 738 → 7 + 3 + 8 = 18
# n=738
# sum=0
# while(n!=0):
#     ld=n%10
#     n=n//10
#     sum=sum+ld
# print(sum)


# 2.Find the average of digits in a given number.
#      Example: 624 → (6 + 2 + 4) / 3 = 4

# n=624
# sum=0
# count=0
# while(n!=0):
#     ld=n%10
#     n=n//10
#     sum=sum+ld
#     count=count+1
#     avg=sum//count
# print(avg)



# 3.Find the sum of the first digit and the last digit of a given number.
#      Example: 936 → 9 + 6 = 15

# n=936
# sum=0
# small=9
# large=0
# while(n!=0):
#     ld=n%10
#     n=n//10
#     if(ld>large):
#         large=ld
#     if(ld<small):
#         small=ld
#     sum=large+small
# print(sum)

# 4.Find the average of digits that are divisible by 5 in a given number.
#      Example: 12575 → Divisible by 5 digits: 5, 5, 5 → Average = (5 + 5 + 5) / 3 = 5


# n=12575896
# sum=0
# count=0
# while(n!=0):
#     ld=n%10
#     n=n//10
#     if(ld%5):
#         sum=sum+ld
#         count=count+1
#         avg=sum//count
# print(avg)
# print(count)



# 5.Find the difference between the largest digit and the smallest digit in a given number.
#      Example: 58321 → Largest = 8, Smallest = 1 → Difference = 8 - 1 = 7


# sub=0
# small=9
# large=0
# while(n!=0):
#     ld=n%10
#     n=n//10
#     if (ld>large):
#         large=ld
#     if(ld<small):
#         small=ld
#     sub=large-small
# print(sub)  


# i=1
# while i<10:
#     print(i)
#     i=i+1


# for i in range(100,150,1):                #palindrome
#     n=i
#     new=n
#     rev=0
#     while n!=0:
#         av=n%10
#         n=n//10
#         rev=rev*10+av
#     if new==rev:
#         print(rev,"palindrome")




# for j in range(1,100001,1):                  #perfect numbers
#     sum=0
#     n=j
#     for i in range(1,n,1):
#         if n%i==0:
#             sum=sum+i
#     if sum==n:
#         print(n)