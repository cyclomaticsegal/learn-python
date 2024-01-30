phone_number = "555 555 1234"
#immutable so new string produced
print(phone_number.replace(" ", "-"))
print(phone_number.replace("5", "9"))
print(phone_number.replace(" ", "-").replace("5", "9"))