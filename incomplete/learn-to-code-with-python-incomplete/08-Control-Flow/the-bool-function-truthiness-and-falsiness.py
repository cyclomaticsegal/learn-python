# with numbers 0 is falsy and any other number is truthy

if 3:
    print("yes truthy, because 3 is not zero")

if 0:
    print("doesn't print because its falsy because its zero")


# a string with one or more charsacters will be considered truthy
    
if "hello":
    print("has characters so it truthy")

if "":
    print("won't print as its an empty string")


#use the bool function to make the truthy of falsy evaluation
    
print(f'bool("") is {bool("")}')
print(f'bool("chars") is {bool("chars")}')
print(f'bool(0) is {bool(0)}')
print(f'bool(1) is {bool(1)}')

