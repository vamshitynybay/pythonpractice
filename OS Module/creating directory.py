import os 
directory= "TYNYBAY-2023"
parent_dir= "C:/Python/"

path= os.path.join(parent_dir,directory)
os.mkdir(path)
print("Directory '% s' created" % directory)
