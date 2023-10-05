
# 0x01. Lockboxes (Algorithm | Python)

## Description

This project provides a Python algorithm to solve the Lockboxes problem. The problem involves determining whether a set of locked boxes can be opened using the provided keys. Each box is numbered sequentially, and the keys correspond to the box numbers. The goal is to check if all boxes can be unlocked starting from an initially unlocked box.

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- The code should be documented
- The code should follow the PEP 8 style (version 1.7.x)
- All files must be executable

## Function

### `canUnlockAll(boxes)`

- Determines whether all boxes can be unlocked.
- `boxes` is a list of lists, where each inner list represents a box and contains the keys to other boxes.
- A key with the same number as a box opens that box.
- The first box, `boxes[0]`, is unlocked initially.
- Returns `True` if all boxes can be opened, else returns `False`.

## Usage

To use the `canUnlockAll` function, follow these steps:

1. Import the function:
   ```python
   from 0-lockboxes import canUnlockAll
   ```

2. Create a list of boxes and call the function with the list as an argument:
   ```python
   boxes = [[1], [2], [3], [4], []]
   result = canUnlockAll(boxes)
   print(result)  # Output: True
   ```

3. Test the function with different sets of boxes and keys to determine if all boxes can be unlocked.

## Example

Here are some example usages of the `canUnlockAll` function:

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

## Author

This algorithm and README.md were created by Tonny Kirwa.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
