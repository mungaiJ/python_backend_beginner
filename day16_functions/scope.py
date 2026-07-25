# ==========================
# 1. LOCAL SCOPE
# ==========================
# A local variable exists only inside the function where it is created.
# It cannot be accessed outside that function.

def my_name():
    user_name = 'Mungai'      # Local variable
    print(user_name)          # Accessible here

my_name()

# print(user_name)           # ❌ Error: user_name only exists inside my_name()



# ==========================
# 2. ENCLOSING SCOPE
# ==========================
# An enclosing scope occurs when one function is defined inside another.
# The inner function can access variables from the outer function.

def morning_message():
    message = 'Good morning people'   # Enclosing variable

    def message_2():
        print(message)                # Accesses the enclosing variable

    message_2()

morning_message()



# ==========================
# 3. NONLOCAL (Modifying Enclosing Scope)
# ==========================
# The inner function can READ variables from the outer function.
# To MODIFY one of those variables, use the 'nonlocal' keyword.

def outer_func():
    msg = 'Hello there!'      # Enclosing variable
    res = ""                  # Enclosing variable

    def inner_func():
        nonlocal res          # Refers to the res in outer_func()
        res = 'How are you?'  # Modifies the outer variable
        print(msg)            # Reads msg from the enclosing scope

    inner_func()

    # res was modified by inner_func()
    print(res)

outer_func()



# ==========================
# 4. GLOBAL SCOPE
# ==========================
# Variables created outside every function are global variables.
# They can be read from inside functions.

my_name = 'Zuriel'           # Global variable

def new_name():
    print(my_name)           # Reads the global variable

new_name()
print(my_name)



# ==========================
# 5. GLOBAL KEYWORD
# ==========================
# Use 'global' when you want to CREATE or MODIFY
# a global variable inside a function.

my_var_1 = 7                 # Global variable

def show_vars():
    global my_var_2          # Creates/uses a global variable
    my_var_2 = 10            # Now my_var_2 exists globally

    print(my_var_1)          # Reads existing global variable
    print(my_var_2)          # Prints the new global variable

show_vars()

# my_var_2 can now be accessed anywhere
print(my_var_2)