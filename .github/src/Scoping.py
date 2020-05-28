#***
#Define a global variable by define the variable name with global
 
def spam():
  global eggs
  eggs = 42
  print(eggs)

spam()
#eggs = 55
print(eggs)