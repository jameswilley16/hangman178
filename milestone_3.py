

# place_holder word variable to check code works
word_choice = "anteater"
  

def check_guess(guess):
    lower_case_guess = guess.lower()
    if lower_case_guess in word_choice:
      print (f'Good guess! {guess} is in the word!')
    else:
      print (f'Sorry, {guess} is not in the word. Try again.')


def ask_for_input():    
  while True:
    guess = input("guess a letter")
    if len(guess) == 1 and guess.isalpha():
        break 
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
  check_guess(guess)

ask_for_input()