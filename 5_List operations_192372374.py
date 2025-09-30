nested_list = [[1, 2, 3], [4, 5, 6]]
print("Nested List:", nested_list)
my_list = [10, 20, 30, 40, 50]
print("\nList:", my_list)
print("Length of list:", len(my_list))
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2
print("\nConcatenation of", list1, "and", list2, ":", concatenated)
print("\nIs 20 in my_list?", 20 in my_list)
print("Is 100 not in my_list?", 100 not in my_list)
print("\nIterating through my_list:")
for item in my_list:
    print(item, end=" ")
print("\n\nFirst element:", my_list[0])
print("Last element:", my_list[-1])
print("\nSlicing examples:")
print("First three elements:", my_list[0:3])
print("Elements from index 2 to end:", my_list[2:])
print("Every second element:", my_list[::2])