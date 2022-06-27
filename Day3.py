## Bill split

# height = input("Please input your head in cm:")
# height_as_int = int(height)
# if height_as_int >= 120:
#     age = input("please input your age:")
#     age_as_int = int(age)
#     if age_as_int <=7:
#         print("you should pay 5$.")
#     elif age_as_int <=12:
#         print("you should pay 7$.")
#     else:
#         print("you should pay 12$.")
# else :
#     print("You can not use Roadrider!")

## bmi 2.0
# height = float(input("Please input your head in m:"))
# weight = float(input("please input your weight in kg:"))
# bmi = round(weight/height**2)
# if bmi < 18.5:
#     print(f"Your bim is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your bmi is {bmi}, you are a normal weight.")
# elif bmi < 30:
#     print(f"Your bmi is {bmi}, you are overweight.")
# elif bmi < 35:
#     print(f"Your bmi is {bmi}, you are obese.")
# else:
#     print(f"Your bmi is {bmi}, you are clinically obese.")

## a year is leap year
## 可以被4整除，但是不能被100整除
## 可以被400整除

# leap year judgement
# year = int(input("Please input the year: "))

# logic one
# if year%400 == 0 :
#     print(f"this year : {year} is a leap year")
# elif year%100 == 0:
#     print(f"this year : {year} is not a leap year")
# elif year%4 == 0:
#     print(f"this year : {year} is a leap year")
# else:
#     print(f"this year :{year} is not a leap year")

# logic two
# if year%4 == 0:
#     if year%100 ==0:
#         if year%400 ==0:
#             print(f"this year : {year} is a leap year")
#         else:
#             print(f"this year : {year} is not a leap year")
#     else :
#         print(f"this year : {year} is a leap year")
# else :
#     print(f"this year : {year} is not a leap year")

# pizza order price
# pizza size S M L, Small $15, Medium $20, Large $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium and Large ：+$3

# Extra cheese for any size : +$1

print("welcome to my pizza store!")
bill = 0
while True:
    size = input("what size pizza do you want? S, M or L : ")
    if size == "S":
        bill += 15
        break
    elif size == "M":
        bill += 20
        break
    elif size == "L":
        bill += 25
        break
    else:
        print("please input right size. S for Small, M for Medium, L for Large , in capital letter")
        continue

while True:
    add_pepperoni= input("Do you want add pepperoni? Y or N : ")
    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3
        break
    elif add_pepperoni == "N":
        bill +=0
        break
    else:
        print("please input Y or N")
        continue

while True:
    extra_cheese = input("Do you want extra cheese? Y or N : ")
    if extra_cheese == "Y":
        bill += 1
        break
    elif extra_cheese == "N":
        bill += 0
        break
    else:
        print("please input Y or N")
        continue

print("your order is: \n")
if size == "L":
    print("Large Pizza")
elif size == "M":
    print("Medium Pizza")
else:
    print("Small Pizza")

if add_pepperoni == "Y":
    print("add pepperoni")
else:
    print("no add pepperoni")

if extra_cheese == "Y":
    print("extra cheese\n")
else:
    print("no extra chesse\n")
print(f"your total bill is ${bill}")