# oloture_sub = open("Oloture.2019.WEBRip.x264-FGT-English.srt", "r")
# counter = 0
# #print(oloture_sub.read())
# for line in oloture_sub.readlines():
#     if "forze speciali" in line.lower():
#        # print("Found -" , line)
#        print("Found in line - " , counter, " - " , line)
    
#     counter += 1 
# print(counter)

# names = ["sule" , "kunle" , "saheed"]


# function_to_map = lambda name:"Mr. " + name #CREATE ANONYMOUS FUNCTION USING LAMBDA


# mapped = map(function_to_map , names) # MAP ANONYMOUS FUNCTION TO LIST NAMES

# print(list(mapped))
# print((mapped))

# names = ["sule" , "kunle" , "saheed"]
# empty_list = []
# for name in names:
#     empty_list.append("Mr. " + name)
# print(empty_list)

# numbers = [23, 54, 31, 90, 34]
# max = 97
#create a new view where each of the number values become percentages of 97

# function_to_map =map(lambda x: round((x/max)*100, 1) , numbers)

# real_view = [str(i)+ "%" for i in function_to_map]

# # print(list(function_to_map))
# print(real_view)

####### TO SOLVE USING MAP#################

daily_sales = [23, 54, 31, 90, 34]
# daily_target = 97
# sales_percentage = map(lambda  sale : f"{round(sale/daily_target*100, 2)}%", daily_sales)
# print(list(sales_percentage))

# ##### TO SOLVE USING LOOPS##############

# sales_percentage = []
# for sale in daily_sales:
#     sales_percentage.append(f"{round(sale/daily_target*100, 2)}%")

######### REDUCE#######

# import functools
# #OR
# from functools import reduce

# reduction_value = reduce( lambda x,y: x*y, daily_sales)

# print(reduction_value)

############ FILTER#######################

results = filter(lambda x: x>20, daily_sales)
print(list(results))

