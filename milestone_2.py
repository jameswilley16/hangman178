import random

word_list = ["apples", "grapes", "pears", "plums", "limes"]
print(word_list)
word = random.choice(word_list)
print(word)
guess = input("enter a single_letter")

if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input")
        
