# 字符转ASCII码 ord()
# ASCII码转字符 chr()
# 如果要使用函数，把声明的函数放在前面，因为python是一步一步执行的。
def code():
    code_letter = input("please input the word you want to code:\n")
    code_number = int(input("input shift number:\n"))

    a = list(code_letter)
    b = list()
    for i in a:
        t = chr(ord(i) + code_number)
        b.append(t)
    print("your coded word is: \n")
    print(''.join(b))
    

def decode():
    decode_letter = input("please input the word you want to decode:\n")
    decode_number = int(input("input shift number:\n"))

    a = list(decode_letter)
    b = list()
    for i in a:
        t = chr(ord(i) - decode_number)
        b.append(t)
    print("your decoded word is: \n")
    print(''.join(b))


print("Welcome to Code/Decode System!")



while True:
    action_command = input("Do you want to Code or Decode:\n")
    if action_command == 'c' or action_command == 'C' or action_command == 'code':
#         code_letter = input("please input the word you want to code:\n")
#         code_number = int(input("input shift number:\n"))

#         a = list(code_letter)
#         b = list()
#         for i in a:
#             t = chr(ord(i) + code_number)
#             b.append(t)
#         print("your coded word is: \n")
#         print(''.join(b))
        code()
        break
    elif action_command == 'd' or action_command == 'D' or action_command == 'decode':
#         decode_letter = input("please input the word you want to decode:\n")
#         decode_number = int(input("input shift number:\n"))

#         a = list(decode_letter)
#         b = list()
#         for i in a:
#             t = chr(ord(i) - decode_number)
#             b.append(t)
#         print("your decoded word is: \n")
#         print(''.join(b))
        decode()
        break
    else:
        print("please input c or C or code for code.")
        print("please input d or D or decode for decode.")
        print("please try again!")



