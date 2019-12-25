#!/usr/bin/python3

import base64

buffersize = 50000
infile = open('rygel.jpg','rb')
baffer = infile.read(buffersize)
image64 = base64.b64encode(baffer)


print (image64)
