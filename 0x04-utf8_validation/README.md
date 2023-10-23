## 0x04. UTF-8 Validation (Algorithm | Python)

## Project Description

This project involves creating a Python script to determine whether a given data set represents a valid UTF-8 encoding. The script should follow specific requirements and constraints.

## Requirements

- Editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All files should end with a newline
- The first line of all files should be `#!/usr/bin/python3`
- A mandatory README.md file at the root of the project folder
- Code should follow PEP 8 style guidelines (version 1.7.x)
- All files must be executable

## Tasks

### 0. UTF-8 Validation (0-validate_utf8.py)

- Write a method that determines if a given data set represents a valid UTF-8 encoding.
- Prototype: `def validUTF8(data)`
- Return `True` if data is a valid UTF-8 encoding, else return `False`.
- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.
- The data will be represented by a list of integers, where each integer represents 1 byte of data. Therefore, you only need to handle the 8 least significant bits of each integer.

## Usage

1. Make sure you have the required environment (Ubuntu 20.04 LTS, Python 3.4.3).
2. Clone the GitHub repository: [alx-interview](https://github.com/tkirwa/alx-interview).
3. Navigate to the `0x04-utf8_validation` directory.

To test the UTF-8 validation script, run the provided `0-main.py` script:

```bash
./0-main.py
```

This will execute the test cases and display the results.

## Author

[Tonny Kirwa](https://github.com/tkirwa)
## Repository

- GitHub repository: [alx-interview](https://github.com/your-username/alx-interview)
- Directory: `0x04-utf8_validation`
- File: `0-validate_utf8.py`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
