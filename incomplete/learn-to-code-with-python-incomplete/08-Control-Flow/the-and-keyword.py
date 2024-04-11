if 5 < 7 and "rain" == "rain":
    print("Both are true")

#this will short circuit because the left of the "and" evaluated false.
if "rain" == "fire" and 5 < 7:
    print("survived the short circuit")

# way to do between
value = 90
if 90 <= value < 100:
    print("value is between 90 and 100")