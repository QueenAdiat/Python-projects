# file = open("financials.csv" , "r")

# # print(file.readline())

# # heading_list = file.readline().split(",")
# # print(heading_list)
# # print(heading_list[5])


# cash_transactions = []

# for line in file.readlines():
#     transaction_type = line.split(",")[7]
    
#     if transaction_type== "Own Bank Che...":
#         print(line.split(",")[5], line.split(",")[8])

#find each company's tax and the summation of all companies tax. Put it in a dictionary

file = open("financials.csv" , "r")
file_lines = file.readlines()
file_lines.pop(0)

# cash_transactions = []
# target_company = "CHI LIMITED"
# total = 0

# for line in file_lines:
#     transaction_type = line.split(",")[7]
#     company_name = line.split(",")[5]
#     amount_paid = float(line.split(",")[6])
    
#     if company_name == target_company:

#         total += amount_paid

# print(target_company, " : \nTotal ==> " , total)

file = open("financials.csv" , "r") 

all_company_names = []

for line in file_lines: 
    
 company_name = line.split(",")[5]
all_company_names.append(company_name)

mylist = all_company_names

myset =set(mylist)

print(myset)

