"""  
# A no pythonic way to do a loop would be:
my_items = ["a", "b", "c"]

i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1
"""

"""
# A little bit better would be:
for i in range(len(my_items)):
    print(my_items[i])

# Even better:
for item in my_items:
    print(item)
"""

# If we need the index it would be nice to use:
for i, item in enumerate(my_items):
    print(i, item)

