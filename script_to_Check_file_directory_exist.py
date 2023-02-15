'''
import os
print(os.path.exists("c:/python"))
'''
import os
filename="C:\Python\hello2.py"

if os.path.exists(filename) and os.path.isfile(filename):
    print("File or Folder exist")
else:
    print("File or Folder doestn't exist")





