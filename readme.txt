# Project Readme

## Overview
This is a simple banking system project implemented in Python, with formal methods and verification practices applied. This file provides the necessary steps for installing required modules, verifying the code, running the application, and testing its functionality.

---

## Prerequisites
Ensure the following software is installed on your system:

1. **Python 3.8 or higher**
   - [Download Python](https://www.python.org/downloads/)
2. **pip** (Python package installer)
   - Installed automatically with Python.

---
he
## Required Modules
To install the necessary modules, run:



```bash
pip install pylint mypy pytest

```

### Modules Explanation
1. **`pylint`**: For code quality and adherence to Python standards.
2. **`mypy`**: For static type checking.
3. **`pytest`**: For running test cases.

---

## Steps to Verify Code

### 1. Run `pylint`
To check code quality, execute:
```bash
pylint banking.py testing.py
```
A score close to 10 indicates good code quality.

### 2. Run `mypy`
To ensure type safety, execute:
```bash
mypy banking.py testing.py
```
Ensure there are no errors in the output.

---

## Steps to Run the Project

1. Ensure all dependencies are installed.
2. Run the `banking.py` file:

```bash
python banking.py
```
3. Follow the interactive menu to:
   - Login to an existing account.
   - Create a new account.
   - Exit the system.

---

## Steps to Test the Project

1. Run the `testing.py` script using `pytest`:

```bash
pytest testing.py
```
2. Check the output to ensure all test cases pass.

---

## Notes
- Account data is stored in `accounts.txt`. Ensure the file exists and is writable.
- For Z-notation specifications, refer to `z-notation specification.ze` and `Z-notation.pdf` for formal definitions.

---

## Troubleshooting
- If `pylint` or `mypy` fails, ensure your Python version and environment match the prerequisites.
- For issues with `pytest`, verify the structure and syntax of test cases.

---

## Conclusion
This project integrates formal methods and Python tooling to ensure robustness and maintainability. Use the provided steps to explore, verify, and test the application.

