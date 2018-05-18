#!usr/bin/env/python3

n = input('Enter a number more than 1\n')
n = int(n)
steps_count = 0
if n % 2 == 0:
    result=n/2 
    steps_count +=1
    if result != 1:
        steps_count +=1
        result=result+1-result
    print('result is ',result)
        
else:
    result = n*3+1
    steps_count +=1
    if result != 1:
        steps_count +=1
        result= result+1-result
    print('result is :',result)

print('the number of steps is',steps_count)

    
    
