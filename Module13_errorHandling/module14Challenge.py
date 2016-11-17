#write code to open and read a file
#allow the user to specify the file name
#add error handling to provide a suitable error message if the file specficied by the user could not be found

import sys

#define variables
fileName = ''

#ask user for file name to open
fileName = input('Enter the file name of the file you want to open: ')

#try to open file name
try : 
    file = open(fileName, 'r')
    fileContent = file.read()
    print('Success! Below is your file contents: ')
    #print file contents
    print(fileContent)

#check error message and print to screen
except :
    error = sys.exc_info()[0]
    print('Sorry. The following error occured:')
    print(error)

#get in the habbit of closing your files after you're done

file.close()
