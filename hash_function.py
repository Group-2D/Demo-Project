import hashlib

def hash(data):
    return hashlib.sha256(str.encode(data)).hexdigest()

def validate(input, data):
    return True if hash(input) == data else False

test = hash("hi")
print(validate("hi", test))