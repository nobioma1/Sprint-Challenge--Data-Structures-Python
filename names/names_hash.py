# Say your code from names.py is to run on an embedded computer with very limited RAM.
# Because of this,
# memory is extremely constrained and you are only allowed to store names in arrays (i.e. Python lists).
# How would you go about optimizing the code under these conditions?
# Try it out and compare your solution to the original runtime.
# (If this solution is less efficient than your original solution,
# include both and label the stretch solution with a comment)

import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

names_dict = {}

for name in names_1:
    names_dict[name.lower()] = name

for name in names_2:
    if name.lower() in names_dict:
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
