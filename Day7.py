import random
from Day7_wordlist import word_list

choose_word = random.choice(word_list)
print(choose_word)
lens = len(choose_word)
underline_word =['_'] * lens
print(underline_word)
count = 0

while ('_' in underline_word) and (count < 6):
    gusse_letter = input("please input a letter: ").lower()
    if gusse_letter in choose_word:
        for i in range(lens):
            if choose_word[i] == gusse_letter:
                underline_word[i] = gusse_letter
    else:
        count += 1
    print(underline_word)
    
if '_' in underline_word:
    print("You Lose!")
else :
    print("You Win!")
