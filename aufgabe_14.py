import base64 
import sys


def byte_xor(ba1, ba2):
    #return bytes(_a^_b for _a,_b in zip(ba1, ba2))
    return "".join([chr(ord(c1)^ord(c2)) for (c1,c2) in zip(text, key)])

#key = byte_xor(string_b, string_b_base64)

#text = "databasename"

text = sys.argv[1]
# key
key = ";>+>=>,:/>,,(0-;"

decrypted_text = byte_xor(text, key)

#print(base64_bytes)
#print(key)

print("Decrypted pwd: ", decrypted_text)
print("Encoded pwd: ", base64.b64encode(key.encode('utf-8')))

print('cmd entry:', sys.argv)

"""
chr(integer_value) returns string representation of a character
chr(102) -> f as string

x = ord("f")
print(x) -> returns 102 as a int 

https://dev.to/nullx33f/xor-encryption-in-python3-51c

"""
