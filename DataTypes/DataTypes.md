
# Python Data Types and Type Casting

## Python Data Types

In Python, data types are classifications that specify the type of data a variable can hold. The main built-in data types in Python are:

### 1. Numeric Types
- **Integer (int)**: Whole numbers without a decimal point. Example: `10`, `-3`, `42`
- **Float (float)**: Numbers with a decimal point. Example: `3.14`, `-0.5`, `2.0`
- **Complex (complex)**: Numbers with a real and imaginary part, expressed with `j` for the imaginary component. Example: `3+4j`, `2-5j`

### 2. Sequence Types
- **String (str)**: Ordered collection of characters, used for text. Strings are enclosed in single `' '` or double `" "` quotes. Example: `"Hello"`, `'World'`
- **List (list)**: Ordered, mutable collection of items. Lists are enclosed in square brackets `[]`. Example: `[1, 2, 3]`, `['apple', 'banana', 'cherry']`
- **Tuple (tuple)**: Ordered, immutable collection of items. Tuples are enclosed in parentheses `()`. Example: `(1, 2, 3)`, `('a', 'b', 'c')`

### 3. Mapping Type
- **Dictionary (dict)**: Unordered collection of key-value pairs. Dictionaries are enclosed in curly braces `{}`. Example: `{'name': 'John', 'age': 30}`

### 4. Set Types
- **Set (set)**: Unordered collection of unique items. Sets are created with curly braces `{}` or by using the `set()` function. Example: `{1, 2, 3}`, `{'apple', 'banana'}`

### 5. Boolean Type
- **Boolean (bool)**: Represents one of two values: `True` or `False`.

## Type Casting

Type casting in Python is the process of converting one data type to another. Python provides built-in functions to cast data types:

- `int()` - Converts a value to an integer.
- `float()` - Converts a value to a float.
- `str()` - Converts a value to a string.
- `list()` - Converts a value to a list.
- `tuple()` - Converts a value to a tuple.
- `set()` - Converts a value to a set.

### Examples of Type Casting

```python
# Casting float to int
x = 5.7
y = int(x)  # y will be 5

# Casting string to float
str_num = "3.14"
num = float(str_num)  # num will be 3.14

# Casting list to tuple
fruits = ['apple', 'banana', 'cherry']
fruits_tuple = tuple(fruits)

# Casting integer to string
number = 100
number_str = str(number)  # number_str will be '100'
```
