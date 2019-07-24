#enter the 2 numbers you want added together
from config import *
from colorama import init
from termcolor import colored
import pyperclip
colour = "green" #edits the colour
init ()
print (colored("enter the first number",colour))
FirstNum = input()
print (colored("enter the second number",colour))
SecondNum = input()
sum = float(FirstNum) + float(SecondNum)
print (colored("your answer is: " + str (sum),colour))
print ('Press c to copy')
choice = input()
if choice.lower() == 'c':
    pyperclip.copy(int(sum))
    print ('copied')
input ()
