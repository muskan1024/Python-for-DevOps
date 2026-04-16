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