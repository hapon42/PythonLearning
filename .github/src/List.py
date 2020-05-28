#sample looping thru a list
"""
for item in [0,1,2,3]:
  print(item)
"""
#List using range to increment 
"""
lt = list(range(0, 100, 2))
print(lt)
"""

#Loop thru list using index
'''
supplies = ['paper', 'pencil', 'coloring pencil', 'earsier']
for i in range(len(supplies)):
  print('index: '+ str(i) + ' ' + supplies[i])
'''
#Multiple assign in list
animal = ['cat', 'dog', 'snake']
animal1, animal2, animal3 = animal
print(animal1 + " " + animal2 + " " + animal3)
