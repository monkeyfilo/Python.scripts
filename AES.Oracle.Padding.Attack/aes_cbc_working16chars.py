#!/usr/bin/python3

import base64

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

import XOR
import math
import binascii
import itertools

class AES_CBC16():
    def __init__(self,key=get_random_bytes(32)):
        
        self.key = key
        #key = b'0123456789ABCDEF'
        #Outout of this function is bytes. Input can be string or bytes
        self._cipher = AES.new(key)
        
    #Pad the password if not in multiples of 16 before encrypting
    def _add_padding(self,data):
        padding = 16 - (len(data) % 16)
        return data + bytearray(padding for _ in range(padding))

    #Remove padding after decryption
    def _check_and_strip_padding(self,data):
        data = bytearray(data)
        expected_padding = data[-1]
        for i in data[len(data) - expected_padding:]:
            if i != expected_padding:
                raise ValueError("Incorrect Padding")

        return data[:len(data) - expected_padding]


    def _split_blocks(self,data):
      
        length = len(data)
        #import math ceiling so there is no dot 0 in the result (i.e not float)
        blocks = []

        #Range is based on length of blocks divided by 16 
        for i in range (math.ceil (length / 16)):
            #Slice blocks by 16. That is, [0:16] [16:32]
            blocks.append (data[i * 16:(i + 1) * 16])
   
        #Returns a list containing plaintext per 16 bytes each   
      
        return blocks     


    def find_last_byte_basic(self,ciphertext):
        ciphertext = bytearray (base64.b64decode(ciphertext))
        blocks = self._split_blocks (ciphertext)

        c_prime = bytearray([b for b in blocks[0]])
        #print (f"c_prime AKA block [0] {c_prime}")
        print(c_prime)
        
        #print(blocks)
        #print (blocks[0][15] + 1)
        #print (blocks[1])
        
        #for byte in range(blocks[0][15] + 1, 256) + range (0, blocks[0] [15] + 1):
        #This means to cover from item 0 to 255 characters (or 256 characters)
        for byte in itertools.chain (range(blocks[0][15] + 1, 256),range (0, blocks[0] [15] + 1)):

            c_prime[15] = byte
            #print (c_prime + blocks[1])
            print (c_prime[15])
            print (blocks[0][15])
            to_test = base64.b64encode(bytes(c_prime + blocks[1]))
            

            try:
                dec = self.decrypt(to_test)
                print (f"byte: {byte}")
                print (f"blocks 0 15: {blocks[0][15]}")
                print (f"Output of XOR byte, 0x01 and blocks [0] [15]: {byte ^ 0x01 ^blocks[0][15]}")
                print("Decrypt details below:")
                #print (dec)
                print()
            
            except:
                pass

        #print (to_test)


    def find_last_byte (self,ciphertext):
        ciphertext = bytearray (base64.b64decode(ciphertext))
        blocks = self._split_blocks (ciphertext)
        c_prime = bytearray([b for b in blocks[0]])
        #print (f"c_prime AKA block [0] {c_prime}")
        #print()
        
        #List type containing bytearrays 0-15
        plaintext_bytes = bytearray([0 for _ in range(16)]) 
        
        for i in range (16):
            expected_padding= bytearray([0 for _ in range(16-i)] + [(i+1) for _ in range(i)])
            c_prime = XOR.xor(XOR.xor(expected_padding, plaintext_bytes), blocks[0])

        #for byte in range(blocks[0][15] + 1, 256) + range (0, blocks[0] [15] + 1):
        #This means to cover from item 0 to 255 characters (or 256 characters)
            for byte in itertools.chain (range(blocks[0][15-1] + 1, 256),range (0, blocks[0] [15-i] + 1)):

                c_prime[15-i] = byte
                to_test = base64.b64encode(bytes(c_prime + blocks[1]))
                
                try:
                    dec = self.decrypt(to_test)
                    #print (f"byte: {byte}")
                    #print (f"blocks 0 15: {blocks[0][15]}")
                    plaintext_bytes[15-i]= (byte ^ (i+1) ^ blocks [0] [15 -i])
                    #print (f"plaintext_bytes: {(plaintext_bytes)}")
                    break
                
                except:
                    pass

        print (''.join([chr(b) for b in plaintext_bytes if b > 16]))
        #(''.join([chr(b) for b in plaintext_bytes if b > 16]))

        #print (to_test)



    def encrypt(self,plaintext):
        #Type cast to bytearray
        #plaintext = str(plaintext)

        plaintext = self._add_padding(bytearray(plaintext,'utf-8'))
        #print (f"plaintext: {len(plaintext)}")
        
        #Split plaintext into 16 byte blocks
        plaintext_blocks = self._split_blocks(plaintext)
        #print(f"plaintext_blocks: {len(plaintext_blocks)}")

        #iv = get_random_bytes(16)
        #iv =(iv)[0:16]
        iv = b'MThisistheIVIV1X'
        #print (len(iv))
        #print (type(iv))

        #print("iv")
        #print(iv)
        
        #Comment this block. Just testing cipher function
        """
        st1 = 'zzzzzzzzzzzzzzzz'
        z = self._cipher.encrypt(st1)
        print(z)
        print (type(z))
        """

        ciphertext_blocks = []
        for i,block in enumerate(plaintext_blocks):
            #print (i,block)
            #print (len(block))
            if i == 0:
                ciphertext_blocks.append(iv)
                #print(iv)
                #print("iv2")
                
                #print (type(bytes(XOR.xor(iv,block))))
                ciphertext_blocks.append(self._cipher.encrypt(bytes(XOR.xor(iv,block))))
                #print (len(ciphertext_blocks))
                
            else:
                ciphertext_blocks.append(self._cipher.encrypt(bytes(XOR.xor(ciphertext_blocks[i],block))))
                #print (len(ciphertext_blocks))
        return  base64.b64encode(b''.join(ciphertext_blocks))
        #This only works on strings (''.join)
        #If you want to work on bytes, use b''.join()
        #base64.b64encode(''.join(ciphertext_blocks))
        #b"".join([a, b])


    def decrypt(self,ciphertext):
        #Ciphertext is b64 encoded string 
        ciphertext = base64.b64decode(ciphertext)

        #Split ciphertext into 16 byte blocks
        ciphertext_blocks = self._split_blocks(ciphertext)
        
        #First 16 bytes  of Ciphertext is IV (unencrypted)
        #Succeeding blocks of 16 is the encypted plaintext
        #Program execution:
        # . Split ciphertext into 16 blocks each
        # . First 16 blocks is IV (no need to decrypt)
        # . Succeeding blocks are decrypted 16 bytes each

        plaintext_blocks = []
        
        for i, blocks in enumerate(ciphertext_blocks):
            if i == 0: 
                
                iv = blocks
               
            
            else:
                      
                #print((bytes(XOR.xor(self._cipher.decrypt(bytes(blocks)),iv))))
                plaintext_blocks.append(bytes(XOR.xor(self._cipher.decrypt(bytes(blocks)),iv)))
                #plaintext_blocks.append(bytes(XOR.xor((self._cipher.decrypt(bytes(blocks)),iv))
                #plaintext_blocks.append(bytes(XOR.xor(self._cipher.decrypt(bytes(blocks)),iv)))
                #plaintext_blocks.append(self._cipher.decrypt(bytes(XOR.xor(ciphertext_blocks[i],block))))
        #print(f"IV is: {iv}")      
        #print (f"Plaintext block pre stripping and joining: {plaintext_blocks}")       
        decr = (self._check_and_strip_padding (b''.join(plaintext_blocks))) 
        dectext = [(chr(b)) for b in decr]

        return ''.join(dectext)

