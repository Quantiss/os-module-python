#we utilize module OS
import os

#path we are looking at
path = 'D:'

#loop through the WALK method
for folderName, subfolders, filenames in os.walk(path):

    #print folder we are in
    print('Folder - ' + folderName + '\n\n')

    #loop through filenames
    for file in filenames:

        #loop through anything bigger then or equal to 100 MB
        while os.path.getsize(file) >= 100:

            #print the file name
            print('Filename - ' + file)

            #print the file size
            print('File Size in MB - ' + str(os.path.getsize(file)))

            #clean up the output
            print('\n')

            #break out of the while loop
            break