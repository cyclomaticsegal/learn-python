count = 0

while count <= 5:
    print(f'count is {count}')
    count += 1


print(count)


invalid_number = True


while invalid_number:
    user_value = int(input("Please enter a number above 10: "))
    if user_value > 10:
        print(f'Thanks that works! {user_value} is a great choice')
        invalid_number = False
    else:
        print(f'{user_value} doesn''t work')

