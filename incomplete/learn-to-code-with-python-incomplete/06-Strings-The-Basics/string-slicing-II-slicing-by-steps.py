alphabet = "abcdefghijklmnopqrstuvwxyz"

print(alphabet[0:10:2]) #start at 0 and jump by two up to 10

#these are the same
print(alphabet[0:26:1])
print(alphabet[0::1])
print(alphabet[::1])

#move backward
print(alphabet[::-3]) #move backward three steps at a time
#print the string backward
print(alphabet[::-1])
