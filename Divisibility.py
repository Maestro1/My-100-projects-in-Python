#usr/bin/env python3
#Python program to find all numbers divisible by 7 but not a multiple of 5 between 2000 and 3200 (both included)
qualified_nums=[]
for num in range(2000,3201):
    if num % 5 != 0 and num%7 == 0:
        qualified_nums.append(num)
    else:
        pass

print(qualified_nums)
    

