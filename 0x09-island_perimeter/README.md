
# 0x09. Island Perimeter

This project is part of the curriculum of software engineering at Holberton School. The main objective is to create a function that calculates the perimeter of an island represented in a 2D grid.

## Requirements

- Allowed editors: vi, vim, emacs

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)

- All files should end with a new line

- The first line of all files should be exactly `#!/usr/bin/python3`

- Code should use the PEP 8 style (version 1.7)

- You are not allowed to import any module

- All modules and functions must be documented

- All files must be executable

## Task

### 0. Island Perimeter

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

- `grid` is a list of list of integers:

- 0 represents water

- 1 represents land

- Each cell is square, with a side length of 1

- Cells are connected horizontally/vertically (not diagonally).

- `grid` is rectangular, with its width and height not exceeding 100

- The grid is completely surrounded by water

- There is only one island (or nothing).

- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## Usage

To run the script, use the following command:

```bash
./0-main.py
```

## Output

The script should output the perimeter of the island in the grid. For example, for the following grid:

```markdown
[
[0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[0, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0]
]
```

The output should be `12`.

## Author

[Tonny Kirwa](https://github.com/tkirwa), Software Engineer at Holberton School
