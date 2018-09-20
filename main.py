import random
from drawhangman import drawhangman

print("Welcome to Hangman!")

def listjoin(list):
  string = ''.join(list)
  return string

def loadnouns():
  wordlist = ""
  file = open("parsednouns.txt")
  wordlist = file.read().splitlines()
  print("Choosing word from list of " + str(len(wordlist) ) )
  return wordlist

def menu():
  start = input("\nType '1' and ENTER to start!")
  if start == "1":
    play()
    return
  else:
    print("Sorry, I didn't catch that!")
    menu()
    return

def play():
  wrongcount = 0
  wordlist = loadnouns()
  chosenword = list(random.choice(wordlist))
  guess = ["_ "] * len(chosenword)
  debugchosen = listjoin(chosenword).replace(" ", "")
  guessed = []
  while wrongcount < 7:
    drawhangman(wrongcount)
    print(listjoin(guess))
    print("Current Guesses: " + str(guessed))
    userinput = input("Guess a letter!")
    if len(userinput) == 1:
      if userinput in guessed:
        print("You've already guessed that!")
        guessed.remove(userinput)
        wrongcount -= 1
      guessed += userinput
      for i in range (0,len(chosenword)):
        if userinput == chosenword[i]:
          guess[i] = userinput + " "
      if userinput not in chosenword:
        print("That's not in the word!")
        wrongcount += 1

    debugguess = listjoin(guess).replace(" ", "")
    if debugguess == debugchosen:
      print("Congratulations, you guessed the word: " + debugguess)
      menu()
  menu()
        
        
    
  
  
menu()
