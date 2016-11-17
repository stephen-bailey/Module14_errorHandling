import sys

firstNumber = float(input('enter first number: '))
secondNumber = float(input('enter second number: '))

try : 
    result = firstNumber / secondNumber
    print(result)

# except code only runs if something goes wrong with the 'try' fucntion
except ZeroDivisionError :
    error = sys.exc_info()[0]
    print('The answer is infinity')
    sys.exit()
except :
    error = sys.exc_info()[0]
    print('Sorry. The following error occured:')
    print(error)

#finally code will always run no matter whether there is an error above or not
finally : 
    print('this code will always run!!!!')

#you can force your program to exit if an error occurs
#use the function sys.exit() in the sys library

#you can also use variables and an if statement to control what happens after an error


