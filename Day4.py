# randomisation
# import random
# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# list
import random
names_string = input("Input the names, seperation with common : ")
names = names_string.split(", ")
random_choice =random.randint(0,len(names)-1)
print(f"{names[random_choice]} will pay today")