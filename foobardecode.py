'''
import base64

MESSAGE = "FlIAHgINDgcBHhlXVVQMEwsKAFUVGUoWHAcNCwoTB1weTU9TTAQdHxEXVFwJUl9LRgsNEh1LTR5S U1FBSQIaEUtcCRwRBwRJR1RVWFoFHBYdBAMOGgYeGVdVVB4PAgQXGVxdSllTTBMPCRYbTUpKVUlL Rh0KEhceFU1SFQQOSUtOUh5OBBtSTBw="

KEY = 'muskanktr99'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))

'''


import base64
from itertools import cycle

message = input("Enter the encrypted message: ")

key = bytes(input("Enter your Google username: "), "utf8")

print(bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key))))
