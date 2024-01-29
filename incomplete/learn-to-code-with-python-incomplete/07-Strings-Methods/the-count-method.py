#count number of times a substring occurs in the string

word = "queueing"

print(word.count("e")) #2
print(word.count("a")) #0
print(word.count("ue")) #2 (the number of times they occur in that sequence)
print(word.count("e") + word.count("u")) #4 (sums the individual counts of each)



