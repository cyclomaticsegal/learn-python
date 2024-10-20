print(3 in [1,3,5,7,9])

def contains(values, target):
    found = False
    for value in values:
        if value == target:
            found = True
            break
    return found


print(contains([1,3,5,7,9], 3))
print(contains([1,3,5,7,9], 6))

