mad_libs = "{} laughed at the {} {}."

print(mad_libs.format("Booby", "green", "alien"))

#index error missing third placeholder
# print(mad_libs.format("Jack", "screamed"))

# extra placeholders ignored
print(mad_libs.format("Booby", "green", "alien", "ignored"))

#explicit positional
mad_libs = "{2} laughed at the {1} {0}."
print(mad_libs.format("Booby", "green", "alien"))