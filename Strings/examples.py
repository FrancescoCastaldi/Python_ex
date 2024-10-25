
# Basic String Manipulation
# Creating a string and applying common methods
text = " Hello, World! "
print("Original text:", text)
print("Uppercase:", text.upper())
print("Stripped text:", text.strip())
print("Replace 'World' with 'Python':", text.replace("World", "Python"))

# String Formatting Examples

# Using f-strings
name = "Francesco"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Using .format() method
print("My name is {} and I am {} years old.".format(name, age))

# Using Old-style formatting
print("My name is %s and I am %d years old." % (name, age))

# Aligning and Padding
number = 123.4567
print(f"Right-aligned (10 spaces): {number:>10.2f}")
print(f"Left-aligned (10 spaces): {number:<10.2f}")
print(f"Centered (10 spaces): {number:^10.2f}")
