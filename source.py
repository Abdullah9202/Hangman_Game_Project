import random
import os
import hangman_Art
import hangman_WordList

# Fuction to clear the terminal
def clear_terminal():
	os.system('cls' if os.name == 'nt' else 'clear')


# Printing the logo
print(hangman_Art.logo)

# Randomly picking and assigining to a variable named chosen_word
chosen_word = random.choice(hangman_WordList.word_list)

print(f"The solution is {chosen_word}")

# Creatign an empty list
display = []

# Using for loop to add dashes to the list according to the chosen_word length
# for letters in chosen_word:
#     display += "_"

# Range based for loop can also be used to input dasehes
for x in range(0, len(chosen_word)):
	display += "_"    

print(display)

# Using while loop
end_of_game = False
total_Lives = 6 # Total tries 
while end_of_game == False:

	# Taking input from the user and storing in variable named guess
	guess = input("Guess the letter : ").lower()

	# Calling clear function
	clear_terminal()

	# Letting the user if the entered word is already guessed
	if guess in display:
		print(f"You have already guessed {guess}")

	# Comparing the user input with the randomly guessed word and assigining to the places of dashes
	for position in range(0, len(chosen_word)):
		letter = chosen_word[position] # For temporarily storing the letter at the current index
		if letter == guess:
			display[position] = letter
			
	if guess not in chosen_word: # Executes 
		total_Lives -= 1
		if total_Lives == 0: # Stopping criteria if user loses
			end_of_game = True
			# Print out
			print("You lose!")
			
	print(display)
	
	print(hangman_Art.stages[total_Lives])
	
	if "_" not in display: # Stopping criteria if user wins
		end_of_game = True
		# Print out
		print("You win!")
