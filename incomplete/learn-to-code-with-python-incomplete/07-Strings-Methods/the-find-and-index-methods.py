isA = "this is a string".find("is a")
print(isA)


browser = "Google Chrome"
print(browser.find("C"))
print(browser.find("z"))

print(browser.find("Chrome", 4, len(browser)))

print(browser.index("Chrome"))
#print(browser.index("z")) #error instead of -1 like find

print(browser.rfind("e")) #e on the end of Chrome


