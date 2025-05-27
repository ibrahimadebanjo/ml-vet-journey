import random 
# This is a guess number for the game
secreteNumber = random.randint(1,20)
print("I am thinking of a Number between 1 and 20")

# Ask the player to guess 6 times
for guessTaken in range(1,7):
    print("take a guess")
    guess = int(input()) 
    if guess < secreteNumber:
        print("Your guess is too low")
    elif guess > secreteNumber:
        print("Your guess is too High")  
    else:
        break      
if guess == secreteNumber:
    print("Good job! You guessed my number in " + str(guessTaken) + "guesses!")
else:
    print("Nope the number i was thinking of was " + str(secreteNumber))    