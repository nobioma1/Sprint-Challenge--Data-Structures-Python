import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# Remove code snippet with time complexity of O(n ^ 2)
# for name_1 in names_1: O(n)
#     for name_2 in names_2: O(n x n)
#         if name_1 == name_2:
#             duplicates.append(name_1) O(n)

# Initialize a BinarySearchTree with first item in the name_1
bst_names_1 = BinarySearchTree(names_1[0])

# Loop through the names_1 items
# Starting from the item after the 1st
for i in range(1, len(names_1)):
    # insert into the BST for name
    bst_names_1.insert(names_1[i])

# Loop the the names in the second list of name
for name in names_2:
    # Using the contains method in the BST
    # Check if the is already in the BST
    if bst_names_1.contains(name):
        # If name in BST append to the duplicates array
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
