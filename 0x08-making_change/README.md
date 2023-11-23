# 0x08. Making Change

## Overview

This project is about creating a Python algorithm to solve a common problem in computer science known as the "Making Change" problem. The problem involves determining the fewest number of coins needed to meet a given amount total.

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Tasks

### 0. Change comes from within

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

Prototype: `def makeChange(coins, total)`
Return: fewest number of coins needed to meet total

- If total is 0 or less, return 0
- If total cannot be met by any number of coins you have, return -1
- coins is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task

## Usage

To run the script, use the following command:

```
./0-main.py
```

## Output

The script should output the minimum number of coins needed to make change for the given total. If it's not possible to make change for the total with the given coins, the script should output -1.

## Author

Tonny Kirwa
