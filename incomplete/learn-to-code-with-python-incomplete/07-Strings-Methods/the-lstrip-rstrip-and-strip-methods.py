empty_space = "          content             "
#strip out space left or right or both
print(empty_space.__len__())

print(empty_space.lstrip().__len__())

print(empty_space.rstrip().__len__())
print(empty_space.strip().__len__())

print("www.python.org".lstrip("w"))

print("www.python.org".rstrip("org")) #removes org from the right
print("www.python.org".lstrip("org")) #doesn't remove org from the right because looks at left end
print("www.python.org".strip("worg"))