
# Directory traversal of two directories to remove the dupliacate file and move the files which are not present in First Directoy #


**There are two programs in this repository.**

   ### 1. traversDirectory.py 

        This program check if a file is present in both the directories then delete the file from one of the directory.

        import os
        from time import sleep


        files1=[]  #This list has been used to store the files of source directory 

        for entry in os.scandir("M:\Photo\img"):     #for each element in source directory
            if entry.is_file():                      #If the element is file                
                files1.append(entry.name)            #add the file name to the list

                #number of files=84


        for file in os.scandir("M:\Photo\Jaipur Trip"):     #for each element in destination directory
            if file.is_file():                              #If the element is file
                fileName=file.name                          #store the filename in a variable
                if fileName in files1:                    #if the file in present in the list. it means there is a dupliacte file
                    #files2.append(file.name)
                    #print("match found")                   
                    os.remove(file)                        # delete the duplicate file from destination directory
                    # before running the code number of files = 1905


    <h1> 2. traversAndMove.py </h1>

            This program check if the file in present in both the directory then delete the file from the source directory else move the file to the destination directory  and delete the sourece directory.
