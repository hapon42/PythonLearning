print('How many cats do you have?')
ans = input()
try:
  if int(ans) >= 5 :
    print(str(ans) + '!, Thats a lot of cats.')
  else:
    print('You have less than 5 cats.')
except ValueError:
  print('You did not input a number.')

 