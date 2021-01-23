## DO COLLECTION OF VALUES JUST ONCE

#Value = input ("please enter values to input : ")
#value_to_integer = int (value)

#print(value_to_integer)

## DO COLLECTION OF VALUES JUST OVER AND OVER 

# while True:
#     value = input ("please enter values to input: ")
#     value_to_integer = float (value)

#     print (value_to_integer)


##DO COLLECTION OF VALUES JUST OVER AND OVER THEN CREATE A LIST WITH COLLECTED NUMBERS

# values_list = []

# while True:

#     value = input ("please enter values to input: ")
#     value_to_integer = float (value)
#     values_list.append (value_to_integer)
#     print (values_list)

##DO COLLECTION OF VALUES JUST OVER AND OVER THEN CREATE A LIST WITH COLLECTED NUMBERS ADD A BREAK POINT

# values_list = []
# import statistics
# import math
# while True:

#     value = input ("please enter values to input when youre done type q: ")
#     if value.lower () == "q" : 
#         break 
#     value_to_integer = float (value)
#     values_list.append (value_to_integer)
#     print("\nNumbers collected : " , len(values_list), "\n")

# print (values_list)
# number_of_samples = len(values_list)

# # mean_of_numbers = sum(values_list)/ len(vaues_list)
# mean_of_numbers = statistics.mean(values_list)
# # print(statistics.mean(values_list))
# # print(statistics.stdev(values_list))
# # print ("MEAN : " , mean_of_numbers)
# x_xbar_map = map(lambda sample: round(sample - mean_of_numbers, 2), values_list)

# x_xbar_values = list (x_xbar_map)
# print(x_xbar_values)

# x_xbar_sqaured_map = map(lambda  sample: round (sample**2), x_xbar_values)
# x_xbar_sqaured_values = list(x_xbar_sqaured_map)
# print(x_xbar_sqaured_values)
# print("\nx_xbar_sqaured : \n" , x_xbar_sqaured_values)

# variance = round (math.sqrt(sum(x_xbar_sqaured_values)/(number_of_samples - 1)))

# print("\nvariance : \nvariance")

# file = open("assignment.csv" , "w")

# file.write("VALUE, X_XBAR, X_BAR_SQ\n")

# print(f"{('VALUE').center(6)} | {('X_XBAR'). center(6)}) |{('X_BAR_SQ').center(6)}")
# print("-"*24)
# for i in range(number_of_samples):
    

#     print(f"{str(values_list[i]). ljust(6)}| {str(x_xbar_values[i]).center(6)}| {str(variance).center(6)}")

#     file.write(f"{values_list[i]}, {x_xbar_values[i]}, {x_xbar_sqaured_values[i]}\n")

# ASSIGNMENT 2

for i in range(100,999):
    number_multiplied_by_three = i*3
    last_digit = str(i) [2]*3
    print(i, number_multiplied_by_three, last_digit,number_multiplied_by_three== int(last_digit))
    if number_multiplied_by_three==int(last_digit):
        break  