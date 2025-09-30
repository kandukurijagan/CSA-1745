my_list = [10, 20, 30]
print("Original List:", my_list)
my_list.append(40)
print("\nAfter append(40):", my_list)
my_list.insert(1, 15)  # Insert 15 at index 1
print("After insert(1, 15):", my_list)
my_list.extend([50, 60, 70])
print("After extend([50, 60, 70]):", my_list)
del my_list[2]  # Delete element at index 2
print("After del my_list[2]:", my_list)
my_list.remove(50)  # Removes the first occurrence of 50
print("After remove(50):", my_list)
popped_item = my_list.pop()
print("After pop():", my_list)
print("Popped item:", popped_item)