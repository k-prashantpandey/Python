# FUNCTIONS
# ---------------------------------------------------------------------
# IF A GROUP OF STATEMENTS IS REPEATEDLY REQUIRED THEN IT IS NOT RECOMMENDED TO WRITE THESE STATEMENTS EVERYTIME SEPERATELY. WE HAVE TO DEFINE THESE STATEMENTS AS A SINGLE UNIT AND WE CAN CALL THAT UNIT ANY NUMBER OF TIME BASED ON OUR REQUIREMENTS WITHOUT REWRITING. THIS UNIT IS NOTHING BUT FUNCTION. THE MAIN ADVANTAGE OF FUNCTIONS IS CODE REUSABILITY.


# TYPES OF FUNCTOINS:
# (i) built_in function:(which comes with python)
# eg- len,type,print,del,list,dict,int,float etc....

# here print and len function in_built function
# print("this is a print function")
# print(len("something")) 


# (ii) user defined function:(we create to fulfill our business requirement):
# def===>

# ex==->
# 8,4 ---> add,sub,mul,div:
# a=8
# b=4
# print("addition :", 8+4)
# print("substraction :", 8-4)
# print("multiplication :", 8*4)
# print("division :", 8/4)



def calculator(a,b):
 print("addition :", a+b)
print("substraction :", a-b)
print("multiplication :", a*b)
print("division :", a/b)

# calculator(4,4)
# calculator(4,-4)



# def greet():
#     return "good evening"
# msg=greet()
# print(msg)



# def greet(name):
#  print("good evening", name)

# greet ("ankit")


# TYPES OF FUNCTION ARGUMENTS:

# (i) positional:
# ORDER SHOULD BE MAINTAIN.
# NO. OF PARAMETER = NO. OF ARGUMENTS


# def greet(firstname, lastname):
#     print("good evening",firstname,lastname)
#     greet("prashant","kumar")
    
    
    
    # NUMBER OF PARAMETER = NUMBER OF ARGUMENTS
# def greet(firstname, lastname):                  # PARAMETER
#  print("good evening",firstname,lastname)
#  greet("prashant","kumar")                       # ARGUMENTS



# KEY ARGUMENTS:
# def greet(firstname, lastname):
#  print("good evening",firstname,lastname)
#  greet(lastname="kumar",firstname="prashant")



# (ii) KEYWORD:]
# ORDER IS NOT IMPORTANT
# NO. OF PARAMETER = NO. OF ARGUMENTS
# KEYWORD ARGUMENTS SHOULD FOLLOW POSITIONAL ARGUMENTS.



# (iii) DEFAULT ARGUMENTS-->
# ORDER IS IMPORTANT
# NO. OF PARAMETER MAY OR MAY NOT BE EQUAL NO. OF ARGUMENTS.
# def greet (firstname="guest"):
#  print("good evening",firstname)
# greet()



# (iv) variable length arguments ->
# def test(**args):
#  print(args)
#  print(type(args))
#  print(len(args))
# test(firstname="india",country="america")