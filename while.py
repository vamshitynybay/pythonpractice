'''
i=0
while 1:
    print("Hello")
    i+=1
    if i==9:
        break


cart=[10,20,600,60,70,550,90]
for item in cart:
    if item>500:
        print("sorry/n we cannot process this order because item is greater than 500 and insurance must be required")
        #break
        continue 
    print("Processing item:",item)


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)



import platform
print(platform.python_version_tuple())



import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))



values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)



filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

color_list = ["Red","Green","White" ,"Black"]
#print( "%s %s"%(color_list[0],color_list[-1]))
print( "%s %s"%(color_list[0],color_list[-1]))
'''
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)