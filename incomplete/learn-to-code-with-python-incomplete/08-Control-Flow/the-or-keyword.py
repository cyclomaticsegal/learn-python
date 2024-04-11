if 5 > 8 or 7 < 11:
    print("ast least one condition is true")

if "cat" == "cat" or "dog" == "dog":
    print("short circuit works here")

if "cat" == "cat" or "dog" == "cat":
    print("short circuit still works here")

if "dog" == "cat" or "cat" == "cat":
    print("no short circuit does NOT works here")

    