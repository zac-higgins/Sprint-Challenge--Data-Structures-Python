import time
import sys
sys.path.append('../../../Data-Structures/binary_search_tree')
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# Replace the nested for loops below with your improvements
bst = BinarySearchTree(names_2[0])
for name in names_2[1:]:
    bst.insert(name)

for item in names_1:
    if bst.contains(item):
        duplicates.append(item)

end_time = time.time()

# ------ Original function runtime of O(n^2) --------#
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# ---------------------------------------------------#

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
stretch_start_time = time.time()
stretch_list = []
def stretchDuplicates():
    combined_set = set(names_1) & set(names_2)
    for item in combined_set:
        stretch_list.append(item)
        

stretchDuplicates()
stretch_end_time = time.time()
duplicates.sort()
stretch_list.sort()

print (f"Regular:\n{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"Stretch:\n{len(stretch_list)} duplicates:\n\n{', '.join(stretch_list)}\n\n")
print (f"runtime of regular solution: {end_time - start_time} seconds")
print (f"runtime of stretch solution: {stretch_end_time - stretch_start_time} seconds")
