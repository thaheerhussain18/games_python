import random
SecretNumber = random.randint(1, 10)
NumGuesses = 0
while True:
	guess = input("Guess a number between 1 and 10: ")
	guess = int(guess)
	NumGuesses += 1
	if guess == SecretNumber:
		print(f"Congratulations! You guessed the number in {NumGuesses} guesses!")
		break
	elif guess < SecretNumber:
		print("Too low! Guess higher.")
	else:
		print("Too high! Guess lower.")

