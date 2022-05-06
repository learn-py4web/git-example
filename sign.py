import hashlib

from secrets import signing_key

print("Welcome to my superb signing program")
s = input("String to encode: ")
h = hashlib.sha256(signing_key.encode('utf-8'))
h.update(s.encode('utf-8'))
print("Signed: {}".format(h.hexdigest()))

