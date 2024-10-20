import sys

print(sys.argv)

word_lengths = 0

for arg in sys.argv[1:]:
    word_lengths += len(arg)

print(f'the number of words is {word_lengths}')

