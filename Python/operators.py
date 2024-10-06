# operator:
# ---------

# operator are simbols that perform certain task.
# verious set of operator in python as follow.



# i. arithmatic operators:
# +,   -,   *,   /,   //,   %,   **



a=10
b=20

# addition:
# print("addition: ", a+b)

# sub:
# print("substraction: ", a-b)

#multiply:
# print("multiplicaton: ", a*b)

# div:
# print("division: ", a/b)

# floor div:
# print("floor division: ", a//b)    #[ given intigeric value ]
      
# modulous div:
# print("modulous division: ", a%b)

# power operator:
# print("poer opertor: ", a**b)       # [ power value ]
 
# print(5**2)  







# ii. RELATIONAL OR COMPARISON OPERATOR:
# --------------------------------------

# <, <=, >, >=, ==, !=


a=10
b=20

# print(a<b)
# print(a<=b)
# print(a>b)
# print(a>=b)
# print(a==b)
# print(a!=b)   

# print(10>=5)








# iii. LOGICAL OPERATOR:
# ----------------------
# AND:

# print(5==5 and "raju"=="raja")
# print(5 and 10)
# print(0 and 10)
# print("true" and "False")


# OR:
    
# print(true or  false)


# NOT: 

# print(not True)    # [ given oposite value ]
# print(not false)






# iv. BITWISE OPERATOR:  [ APPLICABLE FOR INT AND BOOL VALUE ONLY.  ]
# ----------------------


# & => BITWISE AND: [ IF BOTH 1 THEN 1 ELSE 0, ( RELATE TO MS PAINT ) ] 

# BINARY NO. OF 5 IS =>  101
# BINARY NO. OF 6 IS =>  110
#                       -----
# BITWISE AND       =>   100  [ 100 IS BINARY NO. OF 4 ]

# THEN 5 & 6 => 4

# print(5 & 6)




# | => BITWISE OR: [ just oposite of bitwise and (&),  IF any 1 then 1 else 0. ]
 
# BINARY NO. OF 5 IS =>  101
# BINARY NO. OF 6 IS =>  110
#                       -----
# BITWISE or        =>   111  [ 111 IS BINARY NO. OF 7]

# THEN 5 & 6 => 7

# print(5|6)




# ^ => bitwise xor: [ if both same then 0 else 1 ]

# BINARY NO. OF 5 IS =>  101
# BINARY NO. OF 6 IS =>  110
#                       -----
# BITWISE or        =>   011  [ 011 IS BINARY NO. OF 3]

# THEN 5 & 6 => 3

# print(5|6)




# ~ => bitwise compliment: [ generate next digit with - simbol. ]

#print(~6)




# >> => binary shift right:
# << => binary shift left:
# [ move right either left. ]

# print(15>>1)
# print(15<<1)




# = => assignment operator:

# a=20
# print(a)









# v. special operator:
# --------------------




# (a). identity operator: 
# IS, IS NOT:


# is:

# a=5
# b=5
# print(a is b)

# check =>
# print("id of a:", id(a))
# print("id of b:", id(b))
# print(5 is 6)  [ false ]


# is not:

# print(5 is not 6)  [ true ]




# (b). membership operator:
# IN, NOT IN:


# in:
# var= "india is great"
# print("great" in var)  [ true ]


# not in:
# var= "india is great"
# print("great not in var")  [ false ]