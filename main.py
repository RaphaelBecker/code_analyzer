import os
import ast

class FunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.function_line_counts = []
        self.function_names = []
        self.function_has_nested_loop = []
        self.function_has_docstring = []

    def visit_FunctionDef(self, node):
        # Reset the loop depth for each new function
        self.loop_depth = 0
        self.has_nested_loop = False

        # Count the lines of code in each function
        start_line = node.lineno
        end_line = max((getattr(stmt, 'lineno', start_line) for stmt in ast.walk(node)), default=start_line)
        line_count = end_line - start_line + 1
        self.function_line_counts.append(line_count)

        # Store the name of the function
        self.function_names.append(node.name)

        # Check if the function has a docstring
        self.function_has_docstring.append(ast.get_docstring(node) is not None)

        # Continue visiting child nodes
        self.generic_visit(node)

        # After visiting all child nodes, store whether the function has a nested loop
        self.function_has_nested_loop.append(self.has_nested_loop)

    # ... (rest of the class remains unchanged)

def analyze_functions(directory):
    function_details = []
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(foldername, filename)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    file_content = file.read()
                    tree = ast.parse(file_content, filename=file_path)
                    visitor = FunctionVisitor()
                    visitor.visit(tree)
                    # Append details of each function in the file
                    for func_name, line_count, has_nested_loop, has_docstring in zip(
                            visitor.function_names, visitor.function_line_counts,
                            visitor.function_has_nested_loop, visitor.function_has_docstring):
                        function_details.append((file_path, func_name, line_count, has_nested_loop, has_docstring))
    return function_details


def main():
    directory = 'C:\\Robert_Koch_project\\SUMO_resa89\\sumo.pipeline'
    function_details = analyze_functions(directory)

    substring_to_remove = "C:\\Robert_Koch_project\\SUMO_resa89\\"

    lines_of_code = []
    nested_loops = []
    no_docstrings = []

    for file_path, func_name, line_count, has_nested_loop, has_docstring in function_details:
        if line_count > 30:
            lines_of_code.append(f'{file_path} - {func_name}: {line_count} lines')
        if has_nested_loop:
            nested_loops.append(f'{file_path} - {func_name} has a nested loop')
        if not has_docstring:
            no_docstrings.append(f'{file_path} - {func_name} does not have a docstring')

    print("Functions with more than 30 lines of code:")
    for loc in lines_of_code:
        print(loc.replace(substring_to_remove, ""))

    print("\nFunctions with nested loops:")
    for nl in nested_loops:
        print(nl.replace(substring_to_remove, ""))

    print("\nFunctions without docstrings:")
    for nd in no_docstrings:
        print(nd.replace(substring_to_remove, ""))


if __name__ == "__main__":
    main()
