import os

def check(command):
    print(os.system(command))
    
print('----------------------------------------------------')
print("***RAM Usage***")
check('free')
print('----------------------------------------------------')
print("***System Usage***")
check('uptime')
print('----------------------------------------------------')
print("Current Kernel name is: ")
check('uname')
print('----------------------------------------------------')

name = input("Enter name: ")

def greet(name):
    print("Hello", name)
    
greet(name)

# -----------------------------------------------------------------------------------------------
# Problem 1: Find the Maximum (Basic)
# Write a function called find_maximum that takes two numbers as arguments and returns the larger of the two.

def find_max(num1, num2):
    maximum = max(num1, num2)
    print(maximum)
    # return max(num1, num2)
find_max(122,9)