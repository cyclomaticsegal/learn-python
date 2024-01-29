def p(text):
    print(text)

p("Hello")
p("Goodbye")
p("OK")

#fails
#p()


def add(a, b):
    print("The sum of", a, "and", b, "is", (a+b))

add(3, 5)
add(a=4, b=6)
add(b=6, a=4)

def add3Nums(a, b, c):
    print("The sum of a b c is", a+b+c)

add3Nums(5, b=10, c=15)

#python inspects the args in order and finds is named and so 5 must be position and then finds b and c as named



