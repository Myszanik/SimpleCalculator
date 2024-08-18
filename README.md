# Simple Calculator

This repository contains a simple graphical calculator application built using Python's `tkinter` library. The calculator provides basic arithmetic operations and has a user-friendly graphical interface.

## Overview

The calculator features a user interface with buttons for digits, arithmetic operations, and additional functions such as clear and evaluate. It is designed to perform basic calculations and handle user input through a graphical interface.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **Special Functions**:
  - `C`: Clears the entire entry field.
  - `CE`: Clears the last character from the entry field.
  - `=`: Evaluates the expression and displays the result.
  - `.`: Allows for decimal point entries.
  - `(` and `)`: Support for parentheses in calculations.

## Requirements

- Python 3.x
- `tkinter` (usually comes pre-installed with Python)

## How to Run

1. **Clone this Repository**:
   ```bash
   git clone https://github.com/yourusername/simple-calculator.git
2. **Navigate to the Project Directory:**:
   ```bash
   cd simple-calculator
3. **Run the Calculator Script**:
   ```bash
   python3 calculator.py

## Code Explanation

- **`Calculator` Class**: Contains the main logic for the calculator GUI.
  - **`__init__(self, master)`**: Initializes the GUI components including the entry field and buttons.
  - **`create_button(self, text, row, column)`**: Creates a button with specified text and places it in the grid layout.
  - **`button_click(self, text)`**: Handles button clicks for digits, operations, and special functions.

- **Main Execution**: Initializes the `tkinter` root window and the `Calculator` class. Starts the main event loop to keep the application running.

```python
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
```

## Usage

- **Digit Buttons**: Click the buttons with digits (0-9) to input numbers.
- **Arithmetic Buttons**: Click the operators (`+`, `-`, `*`, `/`) to perform arithmetic operations.
- **Special Buttons**:
  - Click `C` to clear the entire entry field.
  - Click `CE` to delete the last character from the entry field.
  - Click `=` to evaluate the expression and display the result.
  - Use `(` and `)` to group parts of the expression.
  - Click `.` to enter decimal points in the numbers.

## Acknowledgements

- `tkinter` for providing a simple and easy-to-use GUI framework for Python.

