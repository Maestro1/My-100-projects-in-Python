#!usr/bin/env/python3

#Program to define two methods
#getString:to get string from console input
#printString:to print the string in upper case
#Includes simple test function to test the class methods

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input('Enter text\n')

    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()
        
