#!/usr/bin/python38

#Parse a list of IP address into a format which can be consumed by Nessus (i.e. comma delimited)
#Sample Input:
"""
172.10.10.1
 172.3.3.4
    174.3.3.2

Output is 
172.10.10.1,172.3.3.4,174.3.3.2
"""

with open('/Users/monkeyfilo/Desktop/TRASH/Lynda/Python.Advanced/Exercise Files/Tester/IP.txt', 'r') as reader:
    # Note: readlines doesn't trim the line endings
    ip1 = reader.readlines()  #Each readline is added in a SINGLE LIST
    #print(ip1)
    
    #Each entry in the SINGLE LIST is created as a separate LIST within a LIST
    #
    lines = [line.split() for line in ip1] 
    print(lines)
    ls =[]
    
    with open('/Users/monkeyfilo/Desktop/TRASH/Lynda/Python.Advanced/Exercise Files/Tester/IP4.txt', 'w') as writer:
            # Alternatively you could use
            # writer.writelines(reversed(AnyCollectionhere))
            
            for i in lines: #Iterate to each list in the Master LIST
               #print(i)
               for x in i: #Iterate to each list 
                  ls.append(i) 
                  print (x)
             #i = i.rstrip ('\n')
                  writer.write(x + ",")
                  
            print (f"Number of IP address parsed to file: {len(ls)}")

    
