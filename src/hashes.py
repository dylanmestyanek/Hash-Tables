import hashlib

n = 10
key = b'swag'
key2 = "hahahaya".encode()
key3 = b"lunchtime"

index1 = hash(key) % 8
index2 = hash(key2) % 8
index3 = hash(key3) % 8
print(index1)
print(index2)
print(index3)

# for i in range(n):
#     print(hash(key))
#     print(hashlib.sha256(key).hexdigest())