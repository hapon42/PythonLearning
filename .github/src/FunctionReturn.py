def AddNumber(number):
  tempNumber = number
  returnNumber = 0
  while tempNumber <= number and tempNumber != 0:
    returnNumber = int(returnNumber) + int(tempNumber)
    tempNumber = tempNumber - 1
  return returnNumber

ans = AddNumber(5)
print(ans)