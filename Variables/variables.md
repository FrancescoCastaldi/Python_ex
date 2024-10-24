
# Python Variables: Documentation and Exercises

This file combines documentation and exercises to help you understand and practice working with variables in Python.

## Documentation

### What Are Variables?

Variables in Python are symbolic names that refer to data. They allow you to store values, which can be manipulated during the execution of a program. Python is dynamically typed, meaning you don’t need to explicitly declare the variable's type; it is inferred from the value assigned to it.

### Declaring Variables

In Python, variables are declared by simply assigning a value to them using the `=` operator.

```python
x = 10
name = "Alice"
is_active = True
```

### Variable Naming Rules

1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
2. The rest of the name can contain letters, digits (0-9), and underscores.
3. Variable names are case-sensitive. For example, `myVar` and `myvar` are two different variables.
4. Avoid using Python reserved keywords like `if`, `else`, `for`, `while`, etc.

### Variable Types

Python supports several data types that can be assigned to variables:

- **Integers**: Whole numbers, e.g., `x = 5`
- **Floats**: Decimal numbers, e.g., `y = 3.14`
- **Strings**: A sequence of characters, e.g., `name = "Alice"`
- **Booleans**: Represents `True` or `False`, e.g., `is_active = True`

You can use the `type()` function to check a variable's type.

```python
age = 25
print(type(age))  # Outputs: <class 'int'>
```

### Reassigning Variables

Variables can be reassigned to different values and even different types.

```python
x = 5   # x is an integer
x = "Hello"  # x is now a string
```

### Constants

By convention, constants are written in uppercase letters. Although Python does not enforce constant values (i.e., they can be reassigned), it is common practice to treat them as immutable values.

```python
PI = 3.14159
```

### Swapping Variables

Python provides a simple way to swap the values of two variables without needing a temporary variable.

```python
x, y = 5, 10
x, y = y, x  # Swaps values of x and y
```

---

## Exercises

These exercises are designed to help you practice working with variables in Python.

### Exercise 1: Basic Variable Assignment

Create three variables: `x`, `y`, and `z`. Assign them the values 5, 10, and 15, respectively. Then, print each variable's value.

**Instructions:**
1. Create variables `x`, `y`, and `z`.
2. Assign values `5`, `10`, and `15` to them.
3. Print the values of all three variables.

```python
x = 5
y = 10
z = 15
print(x, y, z)
```

### Exercise 2: Variable Types

Create a variable for each of the following data types: string, integer, float, and boolean. Assign appropriate values and print each variable along with its type.

**Instructions:**
1. Create variables `a`, `b`, `c`, and `d` for string, integer, float, and boolean values.
2. Use the `type()` function to print both the value and its data type.

```python
a = "Hello, Python"
b = 42
c = 3.14
d = True
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
```

### Exercise 3: Swapping Variables

Swap the values of two variables, `x` and `y`, without using a temporary variable. Print their values before and after the swap.

**Instructions:**
1. Create variables `x` and `y`.
2. Swap their values without using a temporary variable.
3. Print the values before and after the swap.

```python
x = 5
y = 10
print("Before swap: x =", x, "y =", y)
x, y = y, x
print("After swap: x =", x, "y =", y)
```

### Exercise 4: Variable Reassignment

Create a variable `num` and assign it an integer value. Then, reassign it to a float value. Print the variable's value and type after each assignment.

**Instructions:**
1. Create the variable `num` and assign it an integer.
2. Reassign `num` to a float.
3. Print the value and type after each assignment.

```python
num = 10
print(num, type(num))
num = 10.5
print(num, type(num))
```

### Exercise 5: Constants

Create a variable that you intend to use as a constant and assign it a value. Use the convention of naming constants with uppercase letters. Then, print the value of the constant.

**Instructions:**
1. Create a constant variable (using uppercase).
2. Assign it a value.
3. Print the value of the constant.

```python
PI = 3.14159
print("PI:", PI)
```

---

### Conclusion

This document provides an overview of how variables work in Python, including examples of how to declare and manipulate them. The exercises should help you gain hands-on experience with variable operations in Python.
