#Program to find the biggest of given 3 numbers from keyboard

n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))
if n1>n2 and n1>n3:
    print("Biggest number is:",n1)
elif n2>n3:
    print("Biggest number is:",n2)
else:
    print("Biggest number is:",n3)


n1=eval(input("Enter First Number:"))
n2=eval(input("Enter Second Number:"))
n3=eval(input("Enter Third Number:"))
if n1>n2 and n1>n3:
    print("Biggest number is:",n1)
elif n2>n3:
    print("Biggest number is:",n2)
else:
    print("Biggest number is:",n3)