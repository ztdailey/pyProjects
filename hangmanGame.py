import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list specified
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)        # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()            # what the user has guessed
    lives = 6                       # number of guesses the user gets

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # telling the user which letters are already guessed
        print('You have already guessed these letters: ', ' '.join(used_letters))

        # what current word is and what letters have been guessed correctly
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list), f'   Lives left = {lives}')

        user_letter = input('Guess a letter:  ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            elif user_letter not in word_letters:
                lives = lives - 1

            if lives == 0:
                print(f'Out of lives! Game over! The word was: {word}')
            elif word_list == word:
                print(f'You got it! The word was: {word}!')

        elif user_letter in used_letters:
            print("You already guessed that letter. Try again!")

        else:
            print('Not a valid letter! Try again.')
hangman()