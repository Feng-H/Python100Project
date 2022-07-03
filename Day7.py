import random
from Day7_wordlist import word_list
words_list = ['apple','branana','watermelon']

choose_word = random.choice(words_list)

print(choose_word)

gusse = input("please input a letter: ").lower()
i = int()
print((len(choose_word)))
if i in range(0,len(choose_word)):
    if gusse == choose_word[i]:
        print("right")
    else:
        print("wrong")