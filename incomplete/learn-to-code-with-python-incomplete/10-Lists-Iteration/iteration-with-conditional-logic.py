values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]
values_with_none = [1, 2, 3, None, 4, 5, None, 6, 7, 8, 9, 10]

def sum_odd_numbers(values):
    sum = 0
    for value in values:
        if value % 2 != 0:
            sum += value
    return sum

print(sum_odd_numbers(values))
print(sum_odd_numbers(other_values))


def get_greatest_number(values):
    greatest = None
    for value in values:
        if value is None:
            continue
        if greatest is None or value > greatest:
            greatest = value
    return greatest

print (get_greatest_number(values))
print (get_greatest_number(other_values))
print (get_greatest_number(values_with_none))

