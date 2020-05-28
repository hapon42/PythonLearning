#This program will guess number 
import random
print('What is your name')
name = input()
secretNumber = random.randint(1, 20)
isGuessNumber = False
print('Hello ' + name + "Guess the number form 1 to 20")
for i in range(1,6):
    print('What is your guess number?')
    guessNumber = input()
    if int(guessNumber) > int(secretNumber):
      print('The number is lower than ' + guessNumber)
    elif int(guessNumber) < int(secretNumber):
      print('The number is higher than ' + guessNumber)
    elif int(guessNumber) == int(secretNumber):
      print('you have guess the right number ' + name + ', the number I selected is ' + str(secretNumber) +' You guess the number in ' + str(i) + 'times')
      guessNumber = True
      break
    else:
      print('You did not input a number')

if isGuessNumber == False:
  print('You did not guess the number I choose, the number is ' + str(secretNumber))
else:
  print('Congrats!')
