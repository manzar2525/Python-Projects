import os
from time import sleep


files1=[]
files2=[]

for entry in os.scandir("M:\Photo\img"):
    if entry.is_file():
        files1.append(entry.name)

        #number of files=84


for file in os.scandir("M:\Photo\Jaipur Trip"):
    if file.is_file():
        fileName=file.name
        if fileName in files1:
            #files2.append(file.name)
            print("match found")
            os.remove(file)
            # before running the code number of files = 1905
