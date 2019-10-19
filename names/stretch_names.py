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

# Because I'm only allowed to use python list I'll use a Binary Search


def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] > target:
            high = middle - 1
        elif arr[middle] < target:
            low = middle + 1
        else:
            return middle

    return -1  # not found


# Binary Search takes in sorted lists
# Sort the names in the first list of names_1
names1_sorted = sorted(names_1)

# for each name in name_2
for name in names_2:
    # use a binary search to check if name in the sorted array of names
    # Which will have a runtime on O(log n) faster than the initial implementation of O(n * n) => O(n ^ 2)
    if binary_search(names1_sorted, name) != -1:
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
