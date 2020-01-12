#!/usr/bin/python3

def xor(ba1,ba2):
   """XOR 2 ByteArrays"""
   ba1 = bytearray (ba1)
   ba2 = bytearray (ba2)
   #print (len(ba1))
   #print (len(ba2))
   listx = []
      

   """Carat ^ symbol means XOR operation"""
  
   """
   #Equivalent functon of the list comprehension statement below (return) 
   for i in range(len(ba1)): 
    z = (ba1[i] ^ ba2[i])
    listx.append(z)
   """

   #Change Return to Print and uncomment RETURN statement below
   #return (bytearray(listx))


   return bytearray(ba1[i] ^ ba2[i] for i in range(len(ba1)))


"""
#Create bytearray One
string1 = "Python789asdfc16"
#print (len(string1))
# string with encoding 'utf-8'
#ba1 = bytearray(string1, 'utf-8')
ba1 = b'Python789asdfc16'
print (type(ba1))
#print(ba1)
#print (type(ba1))


#Create bytearray Two
string2 = "Cobra68912wsre16"
#print (len(string2))
# string with encoding 'utf-8'
ba2 = bytearray(string2, 'utf-8')
#print(ba2)


#Call the function
a=bytearray()
a = xor(ba1,ba2)
print(a)
#print(len(a))
"""
