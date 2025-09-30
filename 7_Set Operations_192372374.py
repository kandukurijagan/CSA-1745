A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("Set A:", A)
print("Set B:", B)
union_set = A | B
print("\nUnion of A and B:", union_set)
intersection_set = A & B
print("Intersection of A and B:", intersection_set)
difference_set = A - B
print("Difference (A - B):", difference_set)
sym_diff_set = A ^ B
print("Symmetric Difference of A and B:", sym_diff_set)
print("\nIs 3 in set A?", 3 in A)
print("Is 6 not in set A?", 6 not in A)
A.add(10)
print("\nAfter adding 10 to set A:", A)
A.remove(2) 
print("After removing 2 from set A:", A)
A.discard(20)
print("After discarding 20 from set A:", A)
print("\nIterating through set A:")
for item in A:
    print(item, end=" ")