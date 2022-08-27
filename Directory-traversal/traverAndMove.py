from fileinput import filename
import os
from time import sleep


sourceDir="M:\Photo\\Solo\\"
destinationDir="M:\Photo\\Jaipur Trip\\"
files1=[]

for entry in os.scandir(destinationDir):
    if entry.is_file():
        #print("file is present")
        files1.append(entry.name)
        
    #number of files in SourceDir=84


for file in os.scandir(sourceDir):
    if file.is_file():
        
        if file.name in files1:
            #files2.append(file.name)
            print("match found")
            os.remove(file.path)
            # number of files in DestinationDir= 1912
        else:
            destinationPath=destinationDir+file.name
            #print(destinationDir)
            #print(destinationPath)
            os.rename(file.path,destinationPath)
