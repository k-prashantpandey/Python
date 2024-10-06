# method of string: 

# i. split("pattern") => split in several small part.
#    return a list

# svar="channel is learn coding, there are 2m subscribers, channel is grothing day by day."
# list_of_string=svar.split(" , ")
# print(list_of_string)


# svar="channel is learn coding, there are 2m subscribers, channel is grothing day by day."
# list_of_string=svar.split(" , ")
# print(list_of_string[-1])








# ii. join(sequence)

# data="hellow world," "welcome to our channel," "plzz do subscribe."
# print(type(data))
# print(''.join(data))









# iii. FIND(psttern)

# find("pattern", "start", "end") => find the positiion of our pattern.
#                                    if pattern not found then it will return -1.

#     ex=>

# info= "A QUICK BROWN FOX JUMP OVER THE LAZY DOG"
# print(info.find('QUICK'))

# info= "A QUICK BROWN FOX JUMP OVER THE LAZY DOG"
# print(info.find('O',11))

# info= "A QUICK BROWN FOX JUMP OVER THE LAZY DOG"
# print(info.find('O',16,-1))








# iv. INDIX("PATTERN","START","END") => Index method is same as find method but it will generate a error if pattern not found.

# info= "a quick brown fox jumps over the lazy dog."
# print(info.index('horse',10))








# v. COUNT("PATTERN","start","end")  => IT WILL RETURN OCCURENCE OF SPECIFIED PATTERN.
#                                       it will generate 0 if pattern not found.
# info= "a quick brown fox jumps over the lazy dog."
# print(info.count('o'))







# vi. strip() => REMOVE LEADING AND TRAILING SPACE.

# info= "            a quick brown fox jumps over the lazy dog."
# print(info.strip())






# vii. REPLACE("OLD PATTERN", "NEW PATTERN") => REPLACE OLD PATTERN WITH NEW ONE.

# info= "a quick brown fox jumps over the lazy dog."
# print(info.replace('o','*'))