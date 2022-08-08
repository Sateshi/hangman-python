import random

def print_word(word,guessList):
    finalWord = ""
    for i in range(len(word)):
        if word[i] in guessList:
            print(word[i],end="")
            finalWord += word[i]

        else:
            print("_",end="")
    return finalWord

wordList = ["ALIXE","JOHAN","CODING","SCHOOL"]
game =  True
word = random.choice(wordList)
guessList = []
healthpoints = 5

print("Welcome to the game")
while(game):
    if(print_word(word,guessList) == word):
        print("\nYou won")
        game = False
        break
    guessLetter = input("\nPlease enter a letter: ").upper()
    if(guessLetter in word):
        guessList.append(guessLetter)
    else:
        print("Wrong")
        healthpoints -= 1
        print('\nYou have', healthpoints, 'tries left.')
        if(healthpoints == 0):
            print("You lost")
            game = False
            break