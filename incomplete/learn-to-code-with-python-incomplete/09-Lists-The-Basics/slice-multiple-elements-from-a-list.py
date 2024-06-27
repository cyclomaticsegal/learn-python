print("programming"[3:6])

muscles = ["Biceps", "Triceps", "Deltoid", "Sartorius"]

print(muscles[1:3]) # from second pos to 1 before the 3rd pos
print(muscles[0:2])
print(muscles[:2])
print(muscles[2:30]) #wont crash just goes to last pos
print(muscles[2:])

print(muscles[-4:-2]) #from -4 to -2 (where -2 will be 1 before the second last)

print(muscles[-3:]) #from 3rd from last to end
print(muscles[:-1]) #from start to 1 from the end

print(muscles[::2]) #go across the full list in increments of 2
print(muscles[::-2])
print(muscles[::-1]) #reverse the list

