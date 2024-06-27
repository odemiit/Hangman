#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#For each letter in the chosen_word, add a "_" to 'display'.
display = []
for word in chosen_word:
  display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
guess = input("Guess a letter: ").lower()

#Loop through each position in the chosen_word; If the letter at that position matches 'guess' then reveal that letter in the display at that position.
start = 0

for letter in chosen_word:
  print(f"Current position: {start}\n Current letter: {letter}\n Guessed letter: {guess}")
  if guess == letter:
    display[start] = guess
  start += 1

print(display)