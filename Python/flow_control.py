# FLOW CONTROL:
# -------------
# [ FLOW CONTROL DISCRIBE THE ORDER IN WHICH STATEMENT WILL BE EXICUTTED AT RUNTIME. ]
# I. => CONDITIONAL STATEMENTS:



# (A). IF ELSE:
# ---------------------------------------------------------------------------------------------------
#user_input= input("enter a number: ")
# user_input= int(user_input)

#            !!!!
#             or
#            !!!!

# user_input= int(input("enter the number: "))

# if user_input %2 == 0:
#  print("number is even")
# else:
#     print("number is odd")





# ASSIGNMENT ===>   MARRIAGE APPLICATION:
# IF AGE =18 THEN  YOU ARE TOO YOUNG FOR MARRY.
# IF AGE =39+ THEN YOU ARE TOO OLD FOR MARRY.

# user_input= eval(input("enter your age: "))

# if user_input == 18:
#     print("you are too young for marry")
# elif user_input >=39:
#  print("you are too old for marry")   
# else:
#  print("as your wish!") 















# (B). iterative statement:
# ---------------------------------------------------------------------------------------------
# (i)   FOR LOOP:

# user_input= eval(input("ENTER THE NUMBER: "))
# for number in range(1,11):
#  print(user_input*number)






#           !!!
# import random:   [ printed different different types of number. ]

# import random
# print(random.random())
# print(random.randint(1,100))
#           !!!






# (ii)  WHILE LOOP:

# import random
# lucky_number= random.randint(1,100) 
# user_input= int(input("ENTER NUMBETR: "))
# while lucky_number!=user_input:
#     if user_input==lucky_number:    
#      print("you won") 
#     else:
#      if user_input>lucky_number:
#       print("too large, try again")
#      elif user_input<lucky_number:
#        print("too small, try again")
#     user_input= int(input("ENTER NUMBETR: "))   
         
         
         
      
      
      
      
#             !!!   
#    PASSWORD IN WHILE LOOP.
#             !!!       
        
        
# password= "PK11"
# input_password= input("ENTER THE PASSWORD: ")
# while input_password!=password:
#     input_password= input("ENTER THE PASSWORD: ")
# else:
#         print("WELCOME, YOU CAN PROCEED")













# (C). TRANSFER STATEMENTS:
# -------------------------------------------------------------------------------------------------

# continue: => continue is used to skip after true and false condition.
# break: => break is used to ending loop when we should stop loop after true and false sudden condition.
# pass: => when we should not be use body part in that case we use pass statement.

# pass===>

# if "a" in "learn coading":
#     pass


# continue=====>

# for num in range (1,11):
#     if num%2==0:
#         continue
#     else:
#         print(num)    [ output = 1,3,5,7,9 ]


# break=====>

# for num in range (1,11):
#     if num%2==0:
#         break
#     else:
#         print(num)     [ outpyt = 1 ]
