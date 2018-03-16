#!/usr/bin/python

for i in range(0,10):
    print("execution of %d" % (i))
    
    
for letter in 'Hello World of Python':
    print ">> ",letter
    
#while loop example
count=1    
while count <=10:
    print count
    count+=1
    
#nested loops example

for i in range(1,10):
    for j in range(1,11):
        print "%d * %d = %d" % (i,j,i*j)
    print "~~~~~~~~~~~~~~~~~"
        
    

