# 0x05. N Queens (Algorithm | Python)

This project contains a Python script that solves the N Queens problem using backtracking.

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Your code should use the PEP 8 style (version 1.7.*)
- All files must be executable

## Task

### 0. N queens

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. This script solves the N queens problem.

#### Usage

```bash
./0-nqueens.py N
```

If the user calls the program with the wrong number of arguments, it prints `Usage: nqueens N`, followed by a new line, and exits with the status 1.

N must be an integer greater or equal to 4. If N is not an integer, the script prints `N must be a number`, followed by a new line, and exits with the status 1. If N is smaller than 4, it prints `N must be at least 4`, followed by a new line, and exits with the status 1.

The program prints every possible solution to the problem, one solution per line. The solutions are not printed in a specific order.

You are only allowed to import the sys module.

#### Example

```bash
./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## Repository

- GitHub repository: [alx-interview]()
- Directory: 0x05-nqueens
- File: 0-nqueens.py
