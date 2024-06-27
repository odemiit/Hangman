#Step 5

import random
import stages
import word_list

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks for each letter in the chosen_word
display = []
for word in chosen_word:
  display += "_"

#Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while "_" in display and lives > 0:
  guess = input("Guess a letter: ").lower()

  #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

  
  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter

  #check if user is wrong
  if guess not in chosen_word:
    #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    lives -= 1

  if lives == 0:
    print("You lose.")
  else:
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
      print("You win.")

  #TODO-2: - Import the stages from hangman_art.py and make this error go away.
  print(stages[lives])
