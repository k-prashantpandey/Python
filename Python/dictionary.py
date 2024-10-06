# DICTIONARY{}:
# ----------------------------------------------------------------------------------------------------------------------------
# WE CAN USE LIST,TUPLE AND SET TO REPRESENT GROUP OBJECT AS A SINGLE INTITY.
# BUT IF WE WANT TO REPRESENT GROUP OF OBJECT AS KEY_VALUE PAIRS THEN WE SHOULD GO FOR DICTIONARY.
# DON'T SUPPORT INDEXING AND SLICING.
# INSERTION ORDER IS PRESERVED.
# HETROENEOUS
# MUTABLE 
# KEYS MUST BE UNIQUE, BUT DUPLICATE VALUE ARE ALLOWED.




# EMPTY DICTIONARY
# var= {}
# var2=dict()
# print(type(var))
# print(type(var2))


# DICT WITH SOME VALUE:
# var={"username" : "ankit", "password": "ankit123"} # [ ====> key values. ]
# print(type(var))
# print(var)


# TO KNOW PARTICULAR KEY VALUE:
# var={"username" : "ankit", "password": "ankit123","username": "ankush"}
# print(var["username"])                      # [<====  GIVEN OUTPUT ONLY UPDATED KEY VALUE SUCH AS NEXT USERNAME. ]


# TO REMOVE KEY_VALUE:
# var={"username" : "ankit", "password": "ankit123", "age": 12, "username": "ankush"}
# print(var.pop('age'))
# print(var)


# TO GET KEY_VALUE:
# var={"username" : "ankit", "password": "ankit123", "age": 12, "username": "ankush"}
# print(var.get('password'))
# temp= var.get('password')
# temp= var.get('passwordqqqqq','not available')
# print(temp)


# TO REMOVE ALL DATA:
# var={"username" : "ankit", "password": "ankit123", "age": 12, "username": "ankush"}
# var.clear()
# print(var)


# TO GET ALL KEYS:
# var={"username" : "ankit", "password": "ankit123", "age": 12, "username": "ankush"}
# print(var.keys())


# TO GET ALL VALUES:
# var={"username" : "ankit", "password": "ankit123", "age": 12, "username": "ankush"}
# print(var.values())


# TO GET BOTH KEYS AND VALUES:
# var={"username" : "ankit", "password": "ankit123", "age": 12, "username": "ankush"}
# print(var.items())


# LOOP IN DICT:
# var={"username" : "ankit", "password": "ankit123", "age": 12, "username": "ankush"}
# for keys,values in var.items():
#     print(keys,values, sep="-")


# ADDING/UPDATING DATA IN DICT:
# var={"username" : "ankit", "password": "ankit123", "username": "ankush"}
# var['age']="20"             # [ adding ]
# var['password']="1234"      # [ updating ]
# print(var)