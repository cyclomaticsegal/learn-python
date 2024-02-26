# mad_libs = "{} laughed at the {} {}."

# print(mad_libs.format("Booby", "green", "alien"))

# #index error missing third placeholder
# # print(mad_libs.format("Jack", "screamed"))

# # extra placeholders ignored
# print(mad_libs.format("Booby", "green", "alien", "ignored"))

# #explicit positional
# mad_libs = "{2} laughed at the {1} {0}."
# print(mad_libs.format("Booby", "green", "alien"))

# #use labels - gives more context than numbers
mad_libs = "{name} laughed at the {adjective} {noun}."
# print(mad_libs.format(name="Booby", adjective="green", noun="alien"))

name = input("Enter a namme: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")

print(mad_libs.format(name=name, adjective=adjective, noun=noun))