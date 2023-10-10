# 0x02. Minimum Operations (Algorithm | Python)

## Introduction

This Python project is designed to solve a specific problem: finding the minimum number of operations needed to create a text file containing a given number of 'H' characters. The only allowed operations are "Copy All" and "Paste." This project provides a Python function, `minOperations(n)`, that calculates the fewest number of operations required to reach the desired number of 'H' characters in the file.

## Task Description

In a text file, you have a single character 'H.' Your text editor can perform two operations:
1. **Copy All**: Copies all the characters in the file to the clipboard.
2. **Paste**: Pastes the contents of the clipboard into the file.

Given an integer `n`, you need to find the fewest number of operations required to achieve exactly `n` 'H' characters in the file.

### Function Prototype

```python
def minOperations(n)
```

### Input

- `n` (integer): The target number of 'H' characters to be achieved.

### Output

- An integer representing the minimum number of operations required to reach `n` 'H' characters in the file.

### Special Condition

- If it's impossible to achieve `n` 'H' characters using the given operations, the function should return `0`.

## Example

Suppose you want to achieve `9` 'H' characters. The sequence of operations would look like this:

1. 'H' (1 operation)
2. 'HH' (Copy All, Paste - 2 operations)
3. 'HHH' (Paste - 1 operation)
4. 'HHHHHH' (Copy All, Paste - 2 operations)
5. 'HHHHHHHHH' (Paste - 1 operation)

The total number of operations is `6`.

## How to Use

To use this Python function, you can import it into your script as shown in the provided `0-main.py` example. Simply call the `minOperations` function with the desired `n` value, and it will return the minimum number of operations required.

```python
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

## Repository Information

- **GitHub Repository:** [alx-interview](https://github.com/tkirwa/alx-interview)
- **Directory:** 0x02-minimum_operations
- **File:** 0-minoperations.py

Make sure to follow the project structure and requirements specified in the project description to ensure compatibility and ease of use.
