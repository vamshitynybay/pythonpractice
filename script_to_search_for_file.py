import os

for dirname, dirpath, filename in os.walk("C:\Python\Python-Scripting\Mastering-Python-Scripting-for-System-Administrators-"):
    for file in filename:
        if file =="line_scatter_plot.py*":
            print(os.path.join(dirname_file))

  