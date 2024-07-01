#Step 5

import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

lives = 6

print(hangman_art.logo)

#Create blanks for each letter in the chosen_word
display = []
for word in chosen_word:
  display += "_"

#Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while "_" in display and lives > 0:
  guess = input("Guess a letter: ").lower()

  #If the user has entered a letter they've already guessed, print the letter and let them know.
  if guess in display:
    print(f"You've already guessed {guess}")
  
  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter

  #check if user is wrong
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1

  if lives == 0:
    print("You lose.")
  else:
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
      print("You win.")

  print(hangman_art.stages[lives])
