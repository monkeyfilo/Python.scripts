#!/usr/bin/python

e_list = [1,3,4,5,0,2]

def second_largest(a):
    largest = None
    secl = None 
    for i in e_list:
        if largest == None:
            largest = i 
        
        elif largest < i:
            secl = largest
            largest = i
            
        print (largest, secl)
