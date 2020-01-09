#!/usr/bin/python38

with open('/Users/IP.txt', 'r') as reader:
    # Note: readlines doesn't trim the line endings
    ip1 = reader.readlines()
    lines = [line.split() for line in ip1]
    print(lines)


    with open('/Users/IP2.txt', 'w') as writer:
            # Alternatively you could use
            # writer.writelines(reversed(dog_breeds))
            
            # Write the dog breeds to the file in reversed order
            for i in lines:
               for x in i:
                  print(type(x))
             #i = i.rstrip ('\n')
                  writer.write(x + ",")
             #writer.write(i)
