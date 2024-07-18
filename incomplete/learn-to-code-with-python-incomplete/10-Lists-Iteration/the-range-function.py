print("-------------SIMPLE EXAMPLES----------------")
for number in range(5):
    print(number)

print("-------------START AND END----------------")
for number in range(3, 9):
    print(number)


print("-------------START AND END AND INTERVAL----------------")
for number in range(3, 9, 2):
    print(number)

print("-------------START AND END BACKWARDS WITH INTERVAL----------------")
for number in range(9, -2, -2): # 9, 7, 5, 3, 1, -1 (NOTE -2 is not included)
    print(number)