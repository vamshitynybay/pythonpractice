#Class
#Function
#Loops
'''
class cal():
    def _init_(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
obj=cal(a,b)
choice=1
while choice!=0:
    print("0. exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",obj.add())
    elif choice==2:
        print("Result: ",obj.sub())
    elif choice==3:
        print("Result: ",obj.mul())
    elif choice==4:
        print("Result: ",(obj.div(),2))
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!")

print()
'''
'''
#input("Enter 2 float values:")
#input("Enter 2 float values:").split(',')
Read 2 int/float values from the keyboard which are specified with , : seperation and print sum

a,b=[int(x)for x in input("Enter 2 int values:").split(',')]
print("The Sum:",a+b)

a,b=[float(x)for x in input("Enter 2 float values:").split(',')]
print("The Sum:",a+b)

a,b,c,d=[int(x)for x in input("Enter 4 int values:").split(':')]
print("The Sum:",a+b+c+d)

'''


import sys
  
print("This is the name of the program:", sys.argv[0])
  
print("Argument List:", str(sys.argv))



    





        
        
        
              
