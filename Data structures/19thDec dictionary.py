############# DICTIONARIES#####################
########## CREATING DICTIONARIES######
#DIRECT cREATION#############

# MY_DICT = {
#     "john": ["singing", "dancing"],
#     "tomisin": ["eating", "dancing"],
#     "james": ["talking", "sleeping"],
# }

# print(MY_DICT)

# scores = {
#     "math":90,
#     "english":77,
#     "physics":68,
# }

# print(scores)

# new_dict ={
#     "happy": "the state of being content and in a good mood",
#     "sad": "the state of being discontent and in a bad mood"
# }
# print(new_dict) 

# names = ["samuel", "lucas", "mary"]
# ages = [34, 21, 19]

# print(list(zip(names, ages)))

my_dict = dict() #empty dictionaries can be created using the dict builtin function

# new_dict = dict(list(zip(names,ages)))  #dictionaries can also be created using a list of list or list of tuples 


# print(new_dict)

############# UPDATING DICTIONARIES ####################

# print(my_dict)
# my_dict["laptops"] = ["hp", "acer", "dell", "toshiba"]
# my_dict ["phones"]= ["apple", "samsung", "nokia"]
# my_dict ["sneakers"] = ["nike air", "jordans", "yezzy's"]

# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

###### UPDATING DICTIOANRY VALUES#####################

import datetime
# print(datetime.date.today())
# print(datetime.datetime.now())
# time_now = datetime.datetime.now()

# print("day : ", time_now.day, "Day name : ", time_now.strftime("%A"))
# print("month: ", time_now.month)
# print("year: ", time_now.year)
# print("hour: ", time_now.hour)
# print("minute: ", time_now.minute)
# print("second: ", time_now.second)

# print(time_now.strftime("%A"))
# print(time_now.strftime("%b %d, %Y %I:%m%p"))  #(-STRPTIME()-) CONVERT TIME FROM DATE OBJECT TO STRING FORMAT OF CHOICE

# sample_date = "20202012"

# print(datetime.datetime. strptime(sample_date, "%Y%d%m"). strftime("%b %d, %I: %M%p"))

import pprint

bio_dict =dict()
while True: 

    name = input("Please enter your name : ")
    age = input("How old are you : ")
    small_talk = input("Please enter a small talk : ")

    time_created= datetime.datetime.now(). strftime("%b %d, %Y %I: %M%p")

    bio_dict[name]= {
        "age" : age,
        "small_talk" : small_talk,
        "time_created": time_created
}

    action = input("Please do you want to add another ?? y/n : ")
    if action == "n":
        break   
# print(name,age)
# print(small_talk)
# print("created at : ", time_created)
pprint.pprint(bio_dict)



