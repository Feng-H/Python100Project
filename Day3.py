height = input("Please input your head in cm:")
height_as_int = int(height)
if height_as_int >= 120:
    age = input("please input your age:")
    age_as_int = int(age)
    if age_as_int <=7:
        print("you should pay 5$.")
    elif age_as_int <=12:
        print("you should pay 7$.")
    else:
        print("you should pay 12$.")
else :
    print("You can not use Roadrider!")