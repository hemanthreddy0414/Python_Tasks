# fname="hero"
# print("before function name ",fname)


# def gbScopeEx():
#     print("inside function name ",fname)

# gbScopeEx()

# print("After function name ",fname)



# def localscope():
#     name="localscope"
#     print("function is ",name)
# localscope()


# def value(name):
#     print("my name is ",name)
# value("localscope with input")



# fname="global"

# def value():
#     fname="local"
#     print("inside the function ",fname)
# value()
# print("outside the function ",fname)


# fname="Hero"
# def value():
#     fname="zero"
#     print("inside the function ",fname)
# value()
# print("outside the function")




# def outerfun():
# #enclosing scope
#     myname="hero"
#     def innerfun():
#         nonlocal myname #by using nonlocal variable to modify outer variable
#         myname="zero"
#         print("inner function",myname)
#     innerfun()
#     print("outer function",myname)
# outerfun()



# myname="akhil"         #global variable
# def globalscope():
#     global myname
#     myname="veggalam"
#     print("my name is ",myname)
# globalscope()


# def enclose():
#     myname="veggalam"
#     def inner():
#         nonlocal myname
#         myname="akhil"
#     inner()
#     print("my name is ",myname)
# enclose()


# import builtins
# print(dir(builtins))

# a="python"
# print(len(a))


# def outer():
#     def inner():
#         print(len("python"))
#     inner()
# outer()


# glo="global"
# def outer():
#     enc="enclose"
#     def inner():
#         inside="inner scope"
        # print("------Data from nested scopes-------")
        # print("global scope ",glo)
        # print("enclose scope ",enc)
        # print("local scope ",inside)

    # inner()
    # print("------Data from nested scopes-------")
    # print("global scope ",glo)
    # print("enclose scope ",enc)
    # print("local scope ",inside)
# outer()
# print("------Data from nested scopes-------")
# print("global scope ",glo)
# print("enclose scope ",enc)
# print("local scope ",inside)