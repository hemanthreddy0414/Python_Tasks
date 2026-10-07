# Part A – Basic Number Patterns

# for j in range(1,6,1):
#     for i in range(1,j+1,1):
#         print(j,end="")
#     print()

# 1
# 22
# 333
# 4444
# 55555


# for j in range(5,0,-1):
#     for i in range(5,j-1,-1):
#         print(j,end="")
#     print()

# 5
# 44
# 333
# 2222
# 11111



# for j in range(1,6,1):
#     for s in range(j,6,1):
#         print(" ",end="")
#     for i in range(1,j+1,1):
#         print(j,end="")
#     print()

#      1
#     22
#    333
#   4444
#  55555



# for j in range(5,0,-1):
#     for s in range(j,6,1):
#         print(" ",end="")
#     for i in range(j,0,-1):
#         print(j,end="")
#     print()

#  55555
#   4444
#    333
#     22
#      1


# for j in range(1,6,1):
#     for s in range(j,6,1):
#         print(" ",end="")
#     for i in range(1,j+1,1):
#         print(j,end="")
#     for k in range(2,j+1,1):
#         print(j,end="")
#     print()

#      1
#     222
#    33333
#   4444444
#  555555555



# for j in range(5,0,-1):
#     for s in range(j,6,1):
#         print(" ",end="")
#     for i in range(j,0,-1):
#         print(j,end="")
#     for k in range(j,1,-1):
#         print(j,end="")
#     print()


#  555555555
#   4444444
#    33333
#     222
#      1




#     5
#    444
#   33333
#  2222222
# 111111111



# for j in range(5,0,-1):
#     for s in range(j,0,-1):
#         print(" ",end="")
#     for i in range(5,j-1,-1):
#         print(j,end="")
#     for v in range(4,j-1,-1):
#         print(j,end="")
#     print()

#      5
#     444
#    33333
#   2222222
#  111111111


# for j in range(1,6,1):
#     for s in range(j,0,-1):
#         print(" ",end="")
#     for i in range(j,6,1):
#         print(j,end="")
#     for v in range(j,5,1):
#         print(j,end="")
#     print()

#  111111111
#   2222222
#    33333
#     444
#      5



# for j in range(1,6,1):
#     for s in range(j,6,1):
#         print(" ",end="")
#     for i in range(j,0,-1):
#         print(i,end="")
#     for v in range(2,j+1,1):
#         print(v,end="")
#     print()



# for j in range(1,6,1):
#     for s in range(j,6,1):
#         print(" ",end="")
#     for i in range(1,j+1,1):
#         print(i,end="")
#     for v in range(j-1,0,-1):
#         print(v,end="")
#     print()
    


# for j in range(1,6,1):
#     for s in range(j,0,-1):
#         print(" ",end="")
#     for i in range(5,j-1,-1):
#         print(i,end="")
#     for v in range(j+1,6,1):
#         print(v,end="")
#     print()


# for j in range(1,6,1):
#     for i in range(1,6,1):
#         if j==1 or j==3 or j==5:
#             print("*",end="")
#         else:
#             print(i,end="")
#     print()

# for j in range(1,6,1):
#     for i in range(1,6,1):
#         if i==1 or i==3 or i==5:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# for j in range(1,8,1):
#     for i in range(1,8,1):
#         if j==1 or i==1 or i==4 or j==4 or j==7 or i==7:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for j in range(1,8,1):
#     for i in range(1,8,1):
#         if j==1 and i<=4 or i==4 or j==7 and i>=4 or j==4 or i==7 and j<=4 or i==1 and j>=4:
#             print("*",end=" ")
#         else:
#             print( " ",end=" ")
#     print()



# for j in range(1,6,1):
#     for i in range(1,6,1):
#         if j==1 and i==1 or j==2 and i==2 or j==3 and i==3 or j==4 and i==4 or j==5 and i==5:
#             print("*",end=" ")
#         else:
#             print(i,end=" ")
#     print()



# for j in range(1,8,1):
#     for i in range(1,10,1):
#         if j==3 or j==5 or i+j==6 or i-j==4 or j-i==2 or i+j==12:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# for j in range(1,5,1):
#     for i in range(1,8,1):
#         if j==i or i+j==8:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# *           * 
#   *       *   
#     *   *     
#       *  



# for j in range(1,8,1):
#     for i in range(1,10,1):
#         if  j==4 and i>1 and i<9 or i+j==6 or i-j==4:
#             print("a",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#         a         
#       a   a       
#     a       a     
#   a a a a a a a   
# a               a 


# for j in range(1,8,1):
#     for i in range(1,10,1):
#         if i==1 or j==1 and i<5 or j==7 and i<5 or j==4 and i<5 or j==2 and i==5 or j==3 and i==5 or j==5 and i==5 or j==6 and i==5:
#             print("b",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# b b b b           
# b       b         
# b       b         
# b b b b           
# b       b         
# b       b         
# b b b b     



# for j in range(1,6,1):
#     for i in range(1,7,1):
#         if i==3 or i+j==4 and j<4:
#             print("1",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#     1       
#   1 1       
# 1   1       
#     1       
#     1      



# for j in range(1,6,1):
#     for i in range(1,5,1):
#         if j==1 or i==4 and j<3 or j==3 or i==1 and j>3 or j==5:
#             print("2",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#   2 2 2 2 
#         2 
#   2 2 2 2 
#   2       
#   2 2 2 2 


# for j in range(1,8,1):
#     for i in range(1,6,1):
#         # if j==1 and i<5 or j==2 and i==5 or j==3 and i==5 or j==4 and i<5 or j==5 and i==5 or j==6 and i==5 or j==7  and i<5:
#         if j==1 or j==4 or j==7 or i==5:
#             print("3",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#     3 3 3 3                   #three
#             3 
#             3 
#     3 3 3 3   
#             3 
#             3 
#     3 3 3 3 


#   3 3 3 3 3 
#           3 
#           3 
#   3 3 3 3 3 
#           3 
#           3 
#   3 3 3 3 3 



# for j in range(1,8,1):
#     for i in range(1,10,1):
#         if j==3 or j==5 or i+j==6 or i-j==4 or j-i==2 or i+j==12:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#         *         
#       *   *       
# * * * * * * * * * 
#   *           *   
# * * * * * * * * * 
#       *   *       
#         *  


# for j in range(1,6,1):
#     for i in range(1,6,1):
#         if j==1 or i+j==6:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#    * * * * * 
#          *   
#        *     
#      *       
#    *      

# vas=150
# while vas<200:
#     print(vas)
#     if vas==185:
#         break
#     vas=vas+1


# for j in range(1,6,1):
#     for s in range(j,6,1):
#         print(" ",end="")
#     for i in range(1,j+1,1):
#         print(i,end="")
#     for v in range(j-1,0,-1):
#         print(v,end="")
#     print()

#      1
#     121
#    12321
#   1234321
#  123454321

# for j in range(1,6,1):
#     for i in range(1,j+1,1):
#         print(i,end=" ")
#     print()



#         1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5 




# for j in range(1,6,1):
#     for i in range(1,j+1,1):
#         print(j,end=" ")
#     print()
    
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 


# for j in range(1,6,1):
#     for i in range(1,j+1,1):
#         print(i,end=" ")
#     print()


# for j in range(1,8,1):
#     for i in range(1,10,1):
#         if j==3 or j==5 or i+j==6 or i-j==4 or j-i==2 or i+j==12:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()