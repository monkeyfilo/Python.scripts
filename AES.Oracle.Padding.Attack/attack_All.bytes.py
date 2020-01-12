import base64
import itertools
import math
from aes_cbc_working16chars import AES_CBC16
import XOR

#Oracle Padding attack max 16 character plaintext

myClass = AES_CBC16()


def _split_blocks(data):
      
        length = len(data)
        
        #import math ceiling so there is no dot 0 in the result (i.e not float)
        blocks = []

        #Range is based on length of blocks divided by 16 
        for i in range (math.ceil (length / 16)):
            #Slice blocks by 16. That is, [0:16] [16:32]
            blocks.append (data[i * 16:(i + 1) * 16])
   
        #Returns a list containing plaintext per 16 bytes each   
        #print (blocks)
        return blocks   




def find_last_byte (ciphertext):
        ciphertext = bytearray (base64.b64decode(ciphertext))
        blocks = _split_blocks (ciphertext)

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
                    dec = myClass.decrypt(to_test)
                    #print (f"byte: {byte}")
                    #print (f"blocks 0 15: {blocks[0][15]}")
                    plaintext_bytes[15-i]= (byte ^ (i+1) ^ blocks [0] [15 -i])
                    print (f"plaintext_bytes: {(plaintext_bytes)}")
                    break
                
                except:
                    pass

        print (''.join([chr(b) for b in plaintext_bytes if b > 16]))
        #(''.join([chr(b) for b in plaintext_bytes if b > 16]))



if __name__ == "__main__":

    ptext = "XthisIsPlaintexsd"
    enc = myClass.encrypt(ptext)
    #print(f"\nEncrypted ptext in B64 encoded bytes: {enc} \n")
    find_last_byte(enc)
