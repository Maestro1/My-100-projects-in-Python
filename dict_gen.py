#usr/bin/env python3
#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.


dictionary={}

upper = int(input('Enter num\n'))

for num in range(upper+1):
    num_value = num * num
    dictionary[num] = num_value

print(dictionary)    


