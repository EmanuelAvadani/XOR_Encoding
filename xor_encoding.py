# Python For Offensive PenTest

import random
import sys

# XOR Encryption

key = ';>+>=>,:/>,,(0-;'

print ('\n' + 'Key length = ' + str (  len(key) ))

#message = 'ipconfig' 
message = sys.argv[1]
print ("Msg is " + message + '\n')


def encode_xor(s1, s2):
 return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])

def get_key():
    return key

enc = encode_xor(message, key)
print ('Encrypted messge is: ' + '\n' + enc + '\n') 


dec = encode_xor(enc, key)
print ('Decrypted messge is: ' + '\n' + dec)
# Very important to test if the decrypted message is the same as the to be encrypted text
# Otherwise the unittests will not work!


