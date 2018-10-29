#!/usr/bin/python

# Function to return the fibonacci series for count of n
def fib(n):
    a=0
    b=1
    for i in range(0,n):
        temp = a
        a = b
        b = temp + b
    return a


for c in range(0,13):        
    print (fib(c))    
        
