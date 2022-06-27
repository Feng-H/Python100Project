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
year = int(input("Please input the year: "))

# logic one
if year%400 == 0 :
    print(f"this year : {year} is a leap year")
elif year%100 == 0:
    print(f"this year : {year} is not a leap year")
elif year%4 == 0:
    print(f"this year : {year} is a leap year")
else:
    print(f"this year :{year} is not a leap year")

# logic two
if year%4 == 0:
    if year%100 ==0:
        if year%400 ==0:
            print(f"this year : {year} is a leap year")
        else:
            print(f"this year : {year} is not a leap year")
    else :
        print(f"this year : {year} is a leap year")
else :
    print(f"this year : {year} is not a leap year")