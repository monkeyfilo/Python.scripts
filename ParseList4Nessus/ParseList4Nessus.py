#!/usr/bin/python38

#Parse a list of IP address into a format which can be consumed by Nessus (i.e. comma delimited)

with open('/Users/monkeyfilo/Desktop/TRASH/Lynda/Python.Advanced/Exercise Files/Tester/IP.txt', 'r') as reader:
    # Note: readlines doesn't trim the line endings
    ip1 = reader.readlines()
    lines = [line.split() for line in ip1]
    #print(lines)
    ls =[]

    with open('/Users/monkeyfilo/Desktop/TRASH/Lynda/Python.Advanced/Exercise Files/Tester/IP2.txt', 'w') as writer:
            # Alternatively you could use
            # writer.writelines(reversed(dog_breeds))
            
            # Write the dog breeds to the file in reversed order
            for i in lines:
               for x in i:
                  ls.append(i)
                  print (x)
             #i = i.rstrip ('\n')
                  writer.write(x + ",")
                  
            print (f"Number of IP address parsed to file: {len(ls)}")
