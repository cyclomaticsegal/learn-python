the_simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]

print(the_simpsons[::-1])

for simp in the_simpsons[::-1]:
    print(f"{simp} has a total of {len(simp)} characters")



#reverse function - returns a generator object
#they dont store the entire list only the next object (performant) like a buffer
print(reversed(the_simpsons)) #show the object type <list_reverseiterator>

for character in reversed(the_simpsons):
    print(f"{character} has a total of {len(character)} characters")

