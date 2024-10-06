#                                         set({}:
#                          set represented with curly bracket{}
#                               duplicates are not allowed.
#                            insertion order is not preserved.
#                        indexing and slicing sre not work in set.
#                             hetroeneous elements are allowed.
#                                    mutable in nature.
#                 set is used store group of unique value as single intity. 
# ----------------------------------------------------------------------------------------------------------------------

# EMPTY SET===>
# svar= set()
# print(type(svar))


# # SET WITH SOME DATA==>
# svar={"ram","shyam","lakshman","python","tinku"}   # [ set give us random order output. ]
# print(type(svar))
# print(svar)



# some important method of set:====>

# ADD METHOD==>
# svar={"ram","shyam","lakshman","python","tinku"}
# svar.add("learn coading")
# print(svar)



# #  update method===>
# svar={"ram","shyam","lakshman","python","tinku"}
# svar.update("dear","ravi","raj") 
# svar.update(["dear","ravi","raj"])  # [ compulssary to given itrable symbol such as [],{},() etc... ] 
# print(svar)



# # remove method====>
# svar={"ram","shyam","lakshman","python","tinku"}
# svar.remove("shyam")
# print(svar)

#                                !!!!
#                         for random deletion
#                                !!!!
# svar={"ram","shyam","lakshman","python","tinku"}
# print(svar.pop())
# print(svar)



# # clear method===>
# svar={"ram","shyam","lakshman","python","tinku"}
# svar.clear()
# print(svar)

# -------------------------------------------------------------------------------------------------------------------------



# union===> all
# var={"ram","shyam","lakshman","python","tinku"}
# var2={'true',123,'mohan',"rajsthan","bihar"}
# print(var.union(var2))
#               OR
# print(var | var2)



# intersection==> common
# var={"ram","shyam","lakshman","python","tinku"}
# var2={'tinku',"ram",123,'mohan',"rajsthan","bihar"}
# print(var.intersection(var2))
#            OR
# print(var & var2)
 
 
 
 #DIFFERENCE===>
# var={"ram","shyam","lakshman","python","tinku"}
# var2={'ram',"tinku",123,'mohan',"rajsthan","bihar"}
# print(var.difference(var2))
#print(var - var2) [ operators are fast empliment data then methods. ]



# symetric===> output without non common data.
# var={"ram","shyam","lakshman","python","tinku"}
# var2={'ram',"tinku",123,'mohan',"rajsthan","bihar"}
# print(var.symmetric_difference(var2))
