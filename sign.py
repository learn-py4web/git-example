# This is an example of how to sign strings in Python.
# Copyright Luca de Alfaro, 2022.

import hashlib

from secrets import signing_key

print("Welcome to my superb signing program")
s = input("String to sign: ")
h = hashlib.sha256(signing_key.encode('utf-8'))
h.update(s.encode('utf-8'))
print("Signature: {}".format(h.hexdigest()))

