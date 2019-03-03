#enter the 2 numbers you want added together
from config import *
from colorama import init
from termcolor import colored
init()
print (colored("enter the first number",colour))
FirstNum = input()
print (colored("enter the second number",colour))
SecondNum = input()
sum = float(FirstNum) + float(SecondNum)
print (colored("your answer is: " + str (sum),colour))
input()
