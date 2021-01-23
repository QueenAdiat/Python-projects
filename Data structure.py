# ###### LISTS - COMMA SEPERATED VALUES INSIDE SQAURE BRACES

# fruits = ["apples" , "potatoes" , "yams"]
# print(fruits)
# print("Variable fruits is of type - :" , type(fruits))

# ####### ADD TO THE FRUITS LIST USING APPEND

# print() #### for space in the output
# fruits.append ("fish")
# print (fruits)

# ##### REMOVE YAMS FROM LIST USING REMOVE METHODS
# print()
# fruits.remove ("yams")
# print(fruits)

# ##### COUNT NUMBER OF ITEMS IN LIST USING COUNT METHOD
# print()
# number_of_times_apples_appears_in_a_list= fruits.count("apples")

# print("Apples ocuurs : " , number_of_times_apples_appears_in_a_list , "times")

# ####### EXTEND, INSERT AND POP###
# print()
# items_to_extend = ("mango" , "melon" , "banana")
# fruits.extend (items_to_extend)
# print(fruits)

# print()
# items_to_insert = "guava"
# fruits.insert(1, items_to_insert)
# print(fruits)

# print()
# fruits.pop(1)
# print(fruits)

# ### INDEXING LISTS
# # print(fruits [1])
# # for i in range (4):
# #     print(fruits[i], " - at position" , i)

# i=0
# while i < 4:
#     print(fruits[i], " - at position" , i)
#     i += 1

#### SLICING LIST
data_list = ["ali" , "benky" , "sule" , 2, 3, 12, 14, True, False, True, False]

# string = data_list [0:3]
# numbers = data_list [3:7]
# booleans = data_list[8:11]
# jumping_steps= data_list[0:12:3]
new_jumping_step = data_list[1:5]
# print("strings List---------->" , string)
# print("Numbers List---------->" , numbers)
# print("BooleansList---------->" , booleans)
print(new_jumping_step)


# index=0
# while index<4:
#     print(new_jumping_step[index], " - at position", index)
#     index+=1

index=0
while index<len(data_list):
    print(data_list[index], " - at position", index)
    index+=2




