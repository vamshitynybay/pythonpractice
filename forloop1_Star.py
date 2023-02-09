n=int(input("Enter the number of rows: "))
for i in range(1,n+1): # i represents row number
    for j in range(1,i+1): # J represents the number of *
        print("*",end=" ")
    print()