
# Python Strings and Print Modes

This repository covers basic to advanced concepts of string manipulation and print formatting in Python. It includes examples and exercises to improve your understanding of how strings work in Python and how to print them effectively.

## Topics Covered

- **String Basics**: Creating and manipulating strings.
- **String Methods**: Commonly used methods like `strip()`, `upper()`, `replace()`, etc.
- **Formatted Strings (f-strings)**: Using f-strings for easy and efficient string formatting.
- **Old-Style Formatting**: Using `%` operator for string formatting.
- **`str.format()` Method**: The `format()` method for detailed string customization.
- **Filters and Modifiers**: Using formatting filters like padding, alignment, precision, etc.

Refer to `examples.py` for hands-on exercises.

## Example Usage

```python
# Using an f-string
name = "Francesco"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Using .format() method
print("My name is {} and I am {} years old.".format(name, age))

# Using Old-style formatting
print("My name is %s and I am %d years old." % (name, age))
```

## Additional Resources
- [Python String Documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
