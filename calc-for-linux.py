#This is a Calculator for addition, subtraction, division, and multiplication.
import os
clear = lambda:os.system('clear')
clear()
import time
print ('---Welcome to the best Calculator for Linux!---')
while True:
    print('(1) Add')
    print('(2) Subtract')
    print('(3) Muntiply')
    print('(4) Divide')
    ask=input('Enter choice:    ')
    print ('\n')
    if ask=='':
        print ('Closing')
        time.sleep(3)
        break
    if ask==('1'):
        enter=float(input('Enter number '))
        print ('\n')
        enter01=float(input('Plus '))
        print ('\n')
        answer=enter+enter01
        print (answer)
        print ('\n')
    elif ask==('2'):
        enter=float(input('Enter number '))
        print ('\n')
        enter01=float(input('Minus '))
        print ('\n')
        answer02=enter-enter01
        print (answer02)
        print ('\n')
    elif ask==('4'):
        enter=float(input('Enter number '))
        print ('\n')
        enter01=float(input('Divided by '))
        print ('\n')
        answer04=enter/enter01
        print (answer04)
        print ('\n')
    elif ask==('3'):
        enter=float(input('Enter number '))
        print ('\n')
        enter01=float(input('Multiplied by '))
        print ('\n')
        answer06=enter*enter01
        print (answer06)
        print ('\n')
    else:
        print ('Try again')
        print('\n')
raise SystemExit
