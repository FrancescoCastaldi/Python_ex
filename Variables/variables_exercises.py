# Variables Exercises

# Exercise 1: Basic Variable Assignment
# Create three variables: x, y, and z. Assign them the values 5, 10, and 15, respectively.
# Then, print each variable's value.

x = 5
y = 10
z = 15
print("Exercise 1:")
print(f"x = {x}, y = {y}, z = {z}")

# Exercise 2: Variable Types
# Create a variable for each of the following data types: string, integer, float, and boolean.
# Assign appropriate values and print each variable along with its type.

a = "Hello, Python"
b = 42
c = 3.14
d = True

print("\nExercise 2:")
print(f"a (string): {a}, type: {type(a)}")
print(f"b (integer): {b}, type: {type(b)}")
print(f"c (float): {c}, type: {type(c)}")
print(f"d (boolean): {d}, type: {type(d)}")

# Exercise 3: Swapping Variables
# Swap the values of two variables, x and y, without using a temporary variable.
# Print their values before and after the swap.

print("\nExercise 3: Before Swap")
print(f"x = {x}, y = {y}")

x, y = y, x  # Swapping

print("After Swap")
print(f"x = {x}, y = {y}")

# Exercise 4: Variable Reassignment
# Create a variable `num` and assign it an integer value. Then, reassign it to a float value.
# Print the variable's value and type after each assignment.

num = 10
print("\nExercise 4:")
print(f"num (initial, integer): {num}, type: {type(num)}")

num = 10.5
print(f"num (reassigned, float): {num}, type: {type(num)}")

# Exercise 5: Constants
# Create a variable that you intend to use as a constant and assign it a value.
# Use the convention of naming constants with uppercase letters.
# Then, print the value of the constant.

PI = 3.14159  # Constant for Pi
print("\nExercise 5:")
print(f"PI: {PI}")
