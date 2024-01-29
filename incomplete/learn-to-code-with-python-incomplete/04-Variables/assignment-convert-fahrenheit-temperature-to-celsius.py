
fah = float(input("Enter the temp in fahrenheit:"))
fah_less_32 = fah - 32
cels = round(fah_less_32 * (5/9), 2)
print(f"The conversion of {fah} to celsius is {cels}")