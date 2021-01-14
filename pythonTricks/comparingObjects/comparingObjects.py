# is vs ==

# == is for compare their things, but not being the same thing.
# is compare if they are the exactly same thing.

a = [1, 2, 3]
b = a

print(a == b)
print(a is b) # Because they are pointing to the same object.

""" 
a[0] = "hello"
print(a)
print(b)
# both are gonna be ["hello", 2, 3]
 """

c = list(a)

print(a)
print(b)
print(c)
# They look the same

print(a == c)
print(a is c)
