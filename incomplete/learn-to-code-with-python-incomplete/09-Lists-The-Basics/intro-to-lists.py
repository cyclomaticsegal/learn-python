# a list is an array - an array is a list (the same thing)

print([])

empty = []
empty = list()

sodas = ["Coke", "Pepsi", "Dr. Pepper"]

print(sodas)
print(len(sodas))

quarterly_revenues = [15000, 12000, 9000, 20000]
print(quarterly_revenues)

stock_prices = [34.3, 89.25]
print(len(stock_prices))


def nested_extraction(lstOflists: 'list[list[any]]', idx: int) -> any:
    return lstOflists[idx][idx]
