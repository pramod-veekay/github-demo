#!/usr/bin/python

#sfile = open("sample.txt","w")
#print "filename is : ",sfile.name
#print "file mode is :",sfile.mode


num_words = 0

with open('sample.txt','r') as f:
    for line in f:
        words = line.split()
        num_words+= len(words)
        print "words in the line:",num_words      
print "No of words: ",num_words
   
'''
with open('sample.txt') as f:
    data = f.read()
    print data
    f.close()
    
with open('filename.txt','a') as f:
    f.write("Hello world! This is the first line of my attempt to write to a file.\n")
    f.write("This is the second line ...\n")
    f.close()
    
with open('filename.txt','r') as f:
    data2=f.read()
    print data2
    f.close()
    
'''