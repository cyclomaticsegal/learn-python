errands = ["Go to gym", "Grab lunch", "Get promoted at work", "Sleep"]

#returns a generator object and can iterated o
print(enumerate(errands))

for i, errand in enumerate(errands):
    print(f"{i}: {errand}")


for i, errand in enumerate(errands, 10):
    print(f"{i}: {errand}")

