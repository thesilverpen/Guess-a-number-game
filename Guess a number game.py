#Guess a number game
#Simple version of game, no bells or whistles


import random
secret = random.randint(1, 100)  
guess = 0
attempts = 0
print("Arg782 has landed on Earth and wants to play a game.")

print("Beware Earthling, I have come to take over your planet. Unless you guess my secret number!")
print("My secret number is between 1 and 100---guess if you dare!!")
print("I will give you 8 attempts.")
print("If you fail--then I will rule over all you humans!!!")

while guess != secret and attempts < 8:
    
    guess = int(input("Guess a number! "))  
    if guess < secret:
        print("Too low, try again if you are brave!")
    elif guess > secret:
        print("Too high, try again if you dare!")

    attempts = attempts + 1  

if guess == secret:
    print("Oh, you nasty human! I must return to my home planet in disgrace.")
else:
    print("Prepare to be my minion, human!")
    print("My secret number is", secret)
    
