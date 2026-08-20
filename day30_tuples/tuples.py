# ============================================================
# 1. CREATING A TUPLE
# ============================================================

user = ('Joe', 34, 'Backend developer')

# Check the type of user
print(type(user))  # Output: <class 'tuple'>

# Access the item at index 1
# Index 0 = Joe
# Index 1 = 34
# Index 2 = Backend developer
print(user[1])  # Output: 34

# Access the last item using negative indexing
print(user[-1])  # Output: Backend developer

# Convert the first item ('Joe') into a tuple of characters
print(tuple(user[0]))  # Output: ('J', 'o', 'e')


# ============================================================
# 2. TUPLE UNPACKING
# ============================================================

# Assign each tuple item to a separate variable
name, age, occupation = user

print(name)  # Output: Joe
print(age)  # Output: 34
print(occupation)  # Output: Backend developer


# ============================================================
# 3. UNPACKING WITH *
# ============================================================

# name gets the first item
# *rest collects the remaining items into a list
name, *rest = user

print(rest)  # Output: [34, 'Backend developer']


# ============================================================
# 4. COUNT - Count how many times an item appears
# ============================================================

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')

# count() tells us how many times 'Rust' appears
print(programming_languages.count('Rust'))  # Output: 2


# ============================================================
# 5. INDEX - Find the position of an item
# ============================================================

# index() finds the position of the first 'Rust'
# The 1 means start searching from index 1
#
# Index positions:
# 0 = Rust
# 1 = Java
# 2 = Python
# 3 = C++
# 4 = Rust
#
# Starting from index 1, Rust is found at index 4
print(programming_languages.index('Rust', 1))  # Output: 4


# ============================================================
# 6. INDEX WITH START AND END
# ============================================================

programming_languages = (
    'Rust',
    'Java',
    'Python',
    'C++',
    'Rust',
    'Python',
    'JavaScript',
    'Python'
)

# Search for 'Python'
# Start searching at index 2
# Stop searching before index 5
#
# Index positions:
# 0 = Rust
# 1 = Java
# 2 = Python   <-- found here
# 3 = C++
# 4 = Rust
# 5 = Python
# 6 = JavaScript
# 7 = Python
print(programming_languages.index('Python', 2, 5))  # Output: 2


# ============================================================
# 7. SORTED - Sort the items in a tuple
# ============================================================

numbers = (13, 2, 78, 3, 45, 67, 18, 7)

# sorted() sorts the numbers from smallest to largest
# IMPORTANT:
# sorted() returns a LIST even when the original is a tuple
print(sorted(numbers))  # Output: [2, 3, 7, 13, 18, 45, 67, 78]