# name = input ("please input your name")
# age = int( input("plase enter your age : "))
# years_of_expereince = int(input("please enter your years of expereince :"))
# current_year = 2020
# year_of_birth = current_year - age
# min_allowable_year_of_birth = 1989
# max_allowable_birth = 2001
# years_of_expereince_for_exception = 3

# response = year_of_birth > min_allowable_year_of_birth and \
#             year_of_birth < max_allowable_birth or \
#             years_of_expereince >= years_of_expereince_for_exception and \
#             not (years_of_expereince > age)

# print("Thank you for applying" , name)
# print(" You met all criteria : ", response)

# PROGRAM TO CHECK TO CHECK IF A WORD CONTAINS ANOTHER WORD
#word = input("please enter base word : ")
#other_word = input("please enter word to check : ")
#print(other_word, "was found : " , other_word in word)
# print(f" 'a' was found {word} : {'a' in word} ")
# print(f" 'e' was found {word} : ", "e" in word )
# print(f" 'i' was found {word} : ", "i" in word )
# print(f" 'o' was found {word} : ", "o" in word )
# print(f" 'u' was found {word} : ", "u" in word )

# if "mr" in word: 
#     print("Good day sir")

# elif "mr" not in word:
#     print("Baba how far...!!")
#if "a" in word : print(True)

names = [("ade", 1985, 'Osun'), ("bola", 1995, 'ogun'), ("johnson", 2000, 'kwara'), ("sam", 1967, 'lagos')]
for name, year_of_birth, state in names:
    age = 2020 - year_of_birth
    template = f"Happy birthday {name} you are amazing and we though of ypu fist today as you turn {age} today we love you {state}."
    print(template)

