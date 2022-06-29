# randomisation
# import random
# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# list
# import random
# names_string = input("Input the names, seperation with common : ")
# names = names_string.split(", ")
# random_choice =random.randint(0,len(names)-1)
# print(f"{names[random_choice]} will pay today")

# Rock Paper Scissors Game
game_image = ["🖐️","✂️","⛰️"]

import random
your_choice = int(input("Input your choice, 0 for Rock, 1 for Paper, 2 for Scissors\n"))
print(f"your choice is : {your_choice}\n")
print(game_image[your_choice])
0
computer_choice = random.randint(0,2)
print(f"computer's choice is : {computer_choice}\n")
print(game_image[computer_choice])

if your_choice == computer_choice:
    print("It is a draw.")
elif your_choice == 0 and computer_choice == 1:
    print("You lose")
elif your_choice == 0 and computer_choice == 2:
    print("You win")
elif your_choice == 1 and computer_choice == 0:
    print("You win")
elif your_choice == 1 and computer_choice == 2:
    print("You lose")
elif your_choice == 2 and computer_choice == 0:
    print("You lose")
elif your_choice == 2 and computer_choice == 1:
    print("You Win")