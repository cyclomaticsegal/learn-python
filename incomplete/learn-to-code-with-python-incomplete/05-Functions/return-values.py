def add(a, b):
    print(a+b)

result = add(3, 5)

#returns None
print(result)

#monkey patched so it will demonstrate the return isn't None
def add(a, b):
    return a+b


result = add(4, 5)

print(result)