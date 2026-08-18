# ============================================================
# 1. APPEND - Adding items to a list
# ============================================================

user_names = ['wantam', 'kinuthia', 'munga', 'paul']
user_age = [24, 78, 45, 32]

# Add one item to the end of the list
user_names.append('obote')
print(user_names)

# Add the entire user_age list as ONE item
# This creates a nested list
user_names.append(user_age)
print(user_names)

# ============================================================
# 2. EXTEND - Adding multiple items to a list
# ============================================================

# Add each item from user_age to user_names
# Unlike append(), extend() does not create a nested list
user_names.extend(user_age)
print(user_names)


# ============================================================
# 3. CHANGING ITEMS IN A LIST
# ============================================================

# Change the item at index 1
user_names[1] = 'wanjiru'
print(user_names)


# ============================================================
# 4. CHECKING IF AN ITEM EXISTS
# ============================================================

# Check whether 'munga' exists in the list
'munga' in user_names


# ============================================================
# 5. DELETING ITEMS
# ============================================================

# Delete the item at index 1
del user_names[1]
print(user_names)

# Access the first item
# Remember: Python starts counting indexes from 0
print(user_names[0])

# Access the second item
print(user_names[1])

# Convert the third item into a list of characters
print(list(user_names[2]))

# Find the number of items in the list
print(len(user_names))


# ============================================================
# 6. NESTED LISTS
# ============================================================

# A list can contain another list
user_details = [
    'wantam',
    25,
    'nairobi',
    ['BMW', 'subaru', 'benz']
]

# Get the number of items in user_details
print(len(user_details))

# Access the nested list containing the cars
print(user_details[3])

# Access 'subaru' inside the nested list
print(user_details[3][1])

# Convert the name 'wantam' into a list of characters
print(list(user_details[0]))


# ============================================================
# 7. LIST UNPACKING
# ============================================================

person = ['wantam', 25, 'nairobi']

# Assign each list item to a separate variable
name, age, place = person

print('name is:', name)
print('you are', age, 'years')
print('you stay in:', place)


# ============================================================
# 8. LIST SLICING
# ============================================================

desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']

# Get items from index 1 up to, but NOT including, index 4
print(desserts[1:4])
# Output: ['Cookies', 'Ice Cream', 'Pie']


# ============================================================
# 9. SLICING WITH A STEP
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

# Start at index 1 and take every second item
print(numbers[1::2])
# Output: [2, 4, 6]


# ============================================================
# 10. INSERT - Add an item at a specific position
# ============================================================

numbers = [1, 2, 3, 4, 5]

# Insert 2.5 at index 2
numbers.insert(2, 2.5)

print(numbers)
# Output: [1, 2, 2.5, 3, 4, 5]


# ============================================================
# 11. REMOVE - Remove an item by VALUE
# ============================================================

numbers = [10, 20, 30, 40, 50, 50, 50]

# Remove the first occurrence of 50
numbers.remove(50)

print(numbers)
# Output: [10, 20, 30, 40, 50, 50]


# ============================================================
# 12. POP - Remove an item by INDEX
# ============================================================

numbers = [1, 2, 3, 4, 5]

# Remove the item at index 1
# Index 1 contains the number 2
numbers.pop(1)

print(numbers)
# Output: [1, 3, 4, 5]


# ============================================================
# 13. CLEAR - Remove ALL items
# ============================================================

numbers = [1, 2, 3, 4, 5]

# Remove everything from the list
numbers.clear()

print(numbers)
# Output: []


# ============================================================
# 14. SORT - Sort the original list
# ============================================================

numbers = [19, 2, 35, 1, 67, 41]

# Sort the list from smallest to largest
numbers.sort()

print(numbers)
# Output: [1, 2, 19, 35, 41, 67]


# ============================================================
# 15. SORTED - Create a NEW sorted list
# ============================================================

numbers = [19, 2, 35, 1, 67, 41]

# sorted() creates a new sorted list
# The original list remains unchanged
sorted_numbers = sorted(numbers)

print(numbers)
# Output: [19, 2, 35, 1, 67, 41]

print(sorted_numbers)
# Output: [1, 2, 19, 35, 41, 67]


# ============================================================
# 16. REVERSE - Reverse the order of a list
# ============================================================

numbers = [6, 5, 4, 3, 2, 1]

# Reverse the original list
numbers.reverse()

print(numbers)
# Output: [1, 2, 3, 4, 5, 6]