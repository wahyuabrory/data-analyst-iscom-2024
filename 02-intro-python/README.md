# 🐍 Introduction to Python

Python is a high-level, interpreted, and general-purpose programming language. It was created by Guido van Rossum and first released in 1991. Python is known for its simplicity and readability. It is a versatile language that is used in various domains such as web development, data science, machine learning, and more.

- Easy to use
- Scripting language
- Open-source
- Multiplatform

## 📃Table of Content

- [📦 Installation](#-installation)
- [🚀 Getting Started](#-getting-started)
- [📝 Syntax](#-syntax)
- [🍎 Variable](#-variable)
- [🌏 Standard Naming Variable](#-standard-naming-variable)
- [🔢 Data Type](#-data-type)
- [➕ Arithmetic Operations](#-arithmetic-operations)
- [🎳 Hands on](#-hands-on)
- [📝 Mini Task](#-mini-task)

## 📦 Installation

Python is available for Windows, Mac OS, and Linux. You can download the latest version of Python from the official website [python.org](https://www.python.org/downloads/).

## 🚀 Getting Started

Python is an interpreted language, which means that it is not compiled before it is run. It is executed line by line. You can run Python code in two ways:

- **Interactive Mode**: You can type Python commands directly into the terminal and see the results immediately.
- **Script Mode**: You can write a Python script in a file with a `.py` extension and run it using the Python interpreter.

## 📝 Syntax

Python syntax is simple and easy to learn. It doesn't require any special characters to end a line or a block of code. Python uses indentation to define code blocks, such as for loops, if-else statements, and functions.

```python
# This is a comment
print("Hello, World!")
```

## 🍎 Variable

Variable is a container for storing data values. It is a way to label data with a descriptive name, so that our programs can be understood more clearly by the reader and ourselves. It possible to us to store data dynamically and easy the programmer to get the data.

```python
name = "Abrory"
gender = Male
weight = 70
```

## 🌏 Standard Naming Variable

- Must start with alphabetical(a-z, A-Z) or underscore(\_) character
- Variable name must only contain letter, number, and underscore. Others character like space, dash, and other symbol are not allowed.
- Variable name is case sensitive. It means that `name` and `Name` are different variable.
- Variable name should be descriptive and meaningful.
- Variable name should be in lowercase and use underscore to separate words.
- Should avoid using reserved words in Python as variable name. For example, `print`, `input`, `for`, `if`, `else`, `while`, `def`, `class`, `return`, `import`, `from`, `as`, `with`, `try`, `except`, `raise`, `assert`, `break`, `continue`, `global`, `nonlocal`, `lambda`, `and`, `or`, `not`, `in`, `is`, `None`, `True`, `False`, `del`, `pass`, `yield`, `async`, `await`, `for`, `from`, `as`, `with`, `try`, `except`, `raise`, `assert`, `break`, `continue`, `global`, `nonlocal`, `lambda`, `and`, `or`, `not`, `in`, `is`, `None`, `True`, `False`, `del`, `pass`, `yield`, `async`, `await`.

## 🔢 Data Type

Data type is a way to identify a value and tell the compiler or interpreter how to deal with it. Python has several built-in data types. Can be declared explicitly with defining data type in the beginning of declaration or implicitly with assign value to a variable.

### Common Data Types

- `integer` (int): a whole number, positive or negative, without decimals, of unlimited length.
- `float`: a number, positive or negative, containing one or more decimals.
- `string` (str): a sequence of characters, enclosed in single or double quotes.
- `boolean` (bool): a binary value, either `True` or `False`.
- `list`: a collection which is ordered and changeable. Allows duplicate members.
- `tuple`: a collection which is ordered and unchangeable. Allows duplicate members.
- `set`: a collection which is unordered and un-indexed. No duplicate members.
- `dictionary` (dict): a collection which is unordered, changeable and indexed. No duplicate members.
- `date` & `datetime` (from `datetime` module): a data type to represent date and time.

### Data Casting

It's the process of converting the value of one data type to another data type. Python has two types of type conversion.

- `Implicit` Type Conversion: Python automatically converts one data type to another data type. This process doesn't need any user involvement.
- `Explicit` Type Conversion: In this process, users convert the data type of an object to required data type.

```python
# Implicit Type Conversion
num_int = 123
num_flo = 1.23
num_new = num_int + num_flo
print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))
print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))
```

```python
# Explicit Type Conversion
num_int = 123
num_str = "456"
num_str = int(num_str)
print("datatype of num_int:",type(num_int))
print("datatype of num_str:",type(num_str))
```

## ➕ Arithmetic Operations

- `Capitalize`

  - `str.capitalize()`: returns a copy of the string with the first character capitalized and the rest lowercased.
  - `uppercase()`: return a copy of the string with all of word capitalized.
  - `lowercase()`: return a copy of the string with all of word lowercased.

- `Concat`

  - `+`
  - `join()`

- `Split`

  - `split()`
  - `rsplit()`

- `Multiplication`

  - `*`

- `Slicing`

  - `[]`
  - `[:]`
  - `[start:]`
  - `[:end]`
  - `[start:end]`
  - `[start:end:step]`

- `Replace`

  - `replace()`

## 🎳 Hands on

[Intro to google colab](/02-intro-python/hands-on%20python.ipynb)

## 📝 Mini Task

Create a program to calculate after price discount. Which the price value is `123.000` and discount value is `23%`. When the code runned it shows

```cmd
Harga asli = Rp. 123.000,-
Diskon = 23%
Harga setelah diskon = Rp. 94.710,-
```
Take a look at [my work](/02-intro-python/discount-app.py)