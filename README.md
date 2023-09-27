# Python Code Analyzer

## Overview

The Python Code Analyzer is a lightweight tool designed to assess and evaluate various characteristics of Python functions within a given project. It navigates through each Python file in the specified directory, extracting details about each function, including the number of lines of code, the presence of nested loops, cyclomatic complexity, the number of function parameters, and any TODO comments in the code.

## Features

- **Lines of Code Counter**: Counts the number of lines in each function and lists functions with more than 30 lines of code.
- **Nested Loop Identifier**: Identifies and lists functions containing nested loops.
- **Cyclomatic Complexity Calculator**: Calculates the cyclomatic complexity of each function and lists those with a complexity greater than 5.
- **Function Parameter Counter**: Counts the number of parameters in each function and lists those with more than 3 parameters.
- **TODO Comment Tracker**: Identifies and lists all the TODO comments present in the code along with their location.

## Usage

1. **Set the Project Directory**: Replace the `directory_absolut_path` variable value in `main()` with the absolute path to the root directory of your Python project.

    ```python
    directory_absolut_path = 'C:\\Your_Project_Directory\\root\\src'
    ```

2. **Check Directory Path**: The script will check if the specified directory path exists. If not, it will exit and print an appropriate error message.

3. **Run the Analyzer**: Execute the Python script.

    ```bash
    python script_name.py
    ```

4. **Review the Output**: The script will print the analysis results to the console, listing:
   - Functions with more than 30 lines of code.
   - Functions containing nested loops.
   - Functions with cyclomatic complexity greater than 5.
   - Functions with more than 3 parameters.
   - TODO comments in the code.

## Dependencies

- **Python**: The script is written in Python and requires Python 3.x to run.
- **AST Module**: Utilizes the Abstract Syntax Tree (AST) module to parse and analyze Python code.
- **OS Module**: Uses the OS module for filesystem navigation and manipulation.

## Contributions

Feel free to contribute to this project by proposing new features, reporting bugs, or enhancing the codebase. Your input is valuable in refining and improving this Python Code Analyzer.
