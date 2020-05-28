import os
print(os.getcwd())

TotalSize = 0
for folder in os.listdir('//home//runner//PythonLearning//.github'):
  if os.path.isfile(os.path.join('//home//runner//PythonLearning//.github', folder)):
    continue
  TotalSize = TotalSize + os.path.getsize(os.path.join('//home//runner//PythonLearning//.github', folder))
print(TotalSize)