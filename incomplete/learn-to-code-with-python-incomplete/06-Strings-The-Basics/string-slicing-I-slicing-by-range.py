address = "Attractive Street, Beverly Hills, CA 90210"

print(address[0:3]) #first three letters of the string
print(address[0:17])
print(address[19:32])
print(address[10:100]) #past the end but python will relax and allow going past



print(address[34:-6])
print(address[-8:-6])


print(address[19:]) #from the 19th to the end
print(address[:-4]) #from fourth last to the start

print(address[:]) #creeates a new copy of the full string (daft)

print("bigfoot"[:2])