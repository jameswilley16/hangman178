import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.list_of_guesses = []
        self.num_letters = len(set(self.word).difference(set(self.word_guessed)))

    def check_guess(self, guess):
        lower_case_guess = guess.lower()

        if lower_case_guess in self.word:
            print(f'Good guess! {lower_case_guess} is in the word.')
            for index, letter in enumerate(self.word):
                if letter == lower_case_guess:
                    self.word_guessed[index] = letter
            self.num_letters -= 1
        else:
            print(f'Try again! {lower_case_guess} is not in the word.')
            self.num_lives -= 1

        self.list_of_guesses.append(lower_case_guess)

        print(f"Lives left: {self.num_lives}")

    def ask_for_input(self):
        while True:
            print("Current word:", ' '.join(self.word_guessed))
            guess = input("Please guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You have already tried that letter.")
            else:
                self.check_guess(guess)
                break

def play_game(word_list):
    game = Hangman(word_list)

    while True:
        if game.num_lives == 0:
            print("You lost! The word was:", game.word)
            break
        if game.num_letters > 0:
           game.ask_for_input()
        if game.num_letters == 0:
            print("Congratulations! You have won the game.")
            break


play_game(["apples", "peach", "anteater", "rabbits", "rugby", "poker", "python", "james", "puppy", "talie"])