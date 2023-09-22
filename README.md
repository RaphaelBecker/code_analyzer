# Python Code Analyzer

## Overview

The Python Code Analyzer is a lightweight tool designed to assess and evaluate various characteristics of Python functions within a given project. It navigates through each Python file in the specified directory and extracts details about each function, such as the number of lines of code, the presence of nested loops, and whether a docstring is provided.

## Features

- **Lines of Code Counter**: Counts the number of lines in each function and lists functions with more than 30 lines of code.
- **Nested Loop Identifier**: Identifies and lists functions containing nested loops.
- **Docstring Checker**: Checks for the presence of docstrings in each function and lists those without docstrings.

## Usage

1. **Set the Project Directory**: Replace the `directory` variable value in `main()` with the path to the root directory of your Python project.

    ```python
    directory = 'C:\\Your_Project_Directory\\'
    ```

2. **Run the Analyzer**: Execute the Python script.

    ```bash
    python script_name.py
    ```

3. **Review the Output**: The script will print the analysis results to the console, listing:
   - Functions with more than 30 lines of code.
   - Functions containing nested loops.
   - Functions lacking docstrings.

## Dependencies

- **Python**: The script is written in Python and requires Python 3.x to run.
- **AST Module**: Utilizes the Abstract Syntax Tree (AST) module to parse and analyze Python code.

## Contributions

Feel free to contribute to this project by proposing new features, reporting bugs, or enhancing the codebase. Your input is valuable in refining and improving this Python Code Analyzer.
