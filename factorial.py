#usr/bin/env python3
#Python Program to compute factorial

#Get user input


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)

num = int(input("Enter Number to get its factorial"))
print(factorial(num))
    
