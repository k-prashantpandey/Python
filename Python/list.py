#                                                  LIST[]
# ---------------------------------------------------------------------------------------------------------------
# LIST IS A DATA  STRACTURE WHERE WE CAN STORE DUPLICATE VALUE AND HETROGENIOUS( INT,FLOAT,BOOL,STR etc.. ) DATA TYPE OBJECTS.
# SLICING AND INDEXING ARE ALSO ALLOWED IN LIST.

# # EMPTY LIST:
# empty_list= []
# print(type(empty_list))


# WITH SOME VALUES
list2= ["akash", "str", "tinku", "7.2", "str", "bool"]
# print(list) 


# WITH LIST():
# list2= ["akash", "str", "tinku", "7.2", "str", "bool"]
# list=list(list2)
# print(list)

 
 
 # PRINT TYPE EMPTY LIST:
# list=list(list2)
# list2= ["akash", "str", "tinku", "7.2", "str", "bool"]
# print(list[2])
# print(list[1:4])



# METHOD OF LIST:
# list2= ["akash", "str", "tinku", "7.2", "str", "bool"]
# print(list2.count("tinku"))



# index:
# list2= ["akash", "str", "tinku", "7.2", "str", "bool","tinku"]
# print(list2.index("tinku"))
# print(list2.index("tinku",4))



# list2= ["kundan","ashish","akash", "str", "tinku", "7.2", "str", "bool"]
# if "akash" in list2:
#     print(list2.index("akash"))
# else:
#     print("not found")



# APPEND===> TO ADD ANY ELEMENT IN LAST OF LIST.
# list2.append("ram")
# list2.append("lakshman")
# print(list2) 



# POP===> TO DELETE AN ELEMENT:
# list2= ["akash", "str", "tinku", "7.2", "str", "bool"]
# list2.pop(1)
# list2.pop(0)
# print(list2)


# INSERT===> to add an element in that positin where we want.
# list2= ["akash", "str", "tinku", "7.2", "str", "bool"]
# list2.insert(1,"kukku",)  
# print(list2)



# extend===> to add list in list:
# list2= ["akash", "str", "tinku", "7.2", "str", "bool"]
# list3= ["random","raju"]
# list2.extend(list3)
# print(list2)


# sort====>
# list2= ["akash", "str", "tinku", "str", "bool"]  # [ sort function always take same type of data such as: all list data are only string. ]
# list2.sort()
# print(list2)


# reverse===>
# list2= ["akash", "str", "tinku", "7.2", "str", "bool"]
# list2.reverse()
# print(list2)


# nested list===> list in list
# list2= ["akash", "str", "tinku", "7.2", "str", "bool",["raju","priya",["ram","mohan",["12","15"]]]]
# print(type(list2))
# print(list2)



#LIST COMPRIHENTION===>
# list2= ["akash", "str", "tinku", "7.2", "str", "bool","aman","arti"]
# a= [ word for word in list2  if word.startswith("a") ]
# print(a)



# copy list===>
# list2= ["akash", "str", "tinku", "7.2", "str", "bool"]
# list3=list2    # [0:3]==> optional
# print(list3)



# list unpacking===>
# list2= ["akash", "str", "tinku","12"]
# name1,name2,name3,number=list2
# print(name1)
# print(name2)
# print(name3)
# print(number)