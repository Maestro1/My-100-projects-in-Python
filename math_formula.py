#! usr/bin/env python3
#Math Program that calculates and prints value according to given formula

import math

#Constant variables
C = 50
H = 30

#variable D should be input as comma separated value
I = input ("Enter comma separated values\n")

#print(I.split(","))
Q=[]
#formula
for d in I.split(","):
    q= math.sqrt((2*C*int(d))/H)
    Q.append(int(q))

# The output should be rounded up 
print(Q)
