# # body mass index  BMI = weight(kg)/height*height(m)
# height = input("enter your height in m: \n")
# weight = input("enter your weight in kg: \n")
# bmi = float(weight)/float(height)**2
# print(bmi)

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give ? 10, 12, or 15? ")
people = input("How many people so split the bill? ")
bill_as_float = float(bill)
tip_as_float = float(tip)
people_as_int = int(people)

result = round(bill_as_float*(1+tip_as_float/100) / people_as_int)

print(f"Each person should pay: $ {result}")