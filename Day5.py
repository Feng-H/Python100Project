import random
from random import shuffle
upper_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
punctuations = ['!','@','#','$','%','^','&','*','(',')','-','=','_','+','`','~']

upper_letters_number = int(input("please input how many upper letters you want: \n"))
lower_letters_number = int(input("please input how many lower letters you want: \n"))
numbers_number = int(input("please input how many numbers you want: \n"))
punctuations_nunmber = int(input("please input how many punctutaions you want: \n"))

password = ""
# easy mode
for i in range(0,upper_letters_number):
    random_number = random.randint(0,25)
    password += upper_letters[random_number]

for i in range(0,lower_letters_number):
    random_number = random.randint(0,25)
    password += lower_letters[random_number]

for i in range(0,numbers_number):
    random_number = random.randint(0,9)
    password += numbers[random_number]

for i in range(0,punctuations_nunmber):
    random_number = random.randint(0,15)
    password += punctuations[random_number]

print(f"your password is : {password}")


def shuffle_str(s):
    # 将字符串转换成列表
    str_list = list(s)
    # 调用random模块的shuffle函数打乱列表
    shuffle(str_list)
    # 将列表转字符串
    return ''.join(str_list)

password_2 = shuffle_str(password)
print(f"your password is : {password_2}")