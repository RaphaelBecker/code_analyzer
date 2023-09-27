import os
import ast

class FunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.function_line_counts = []
        self.function_names = []
        self.function_has_nested_loop = []
        self.function_cyclomatic_complexity = []
        self.function_parameter_count = []

    def visit_FunctionDef(self, node):
        # Initialize metrics for each function
        self.loop_depth = 0
        self.has_nested_loop = False
        self.cyclomatic_complexity = 1  # Start with 1 as per the definition of Cyclomatic Complexity

        # Count the lines of code in each function
        start_line = node.lineno
        end_line = max((getattr(stmt, 'lineno', start_line) for stmt in ast.walk(node)), default=start_line)
        line_count = end_line - start_line + 1
        self.function_line_counts.append(line_count)

        # Store the name of the function
        self.function_names.append(node.name)

        # Count the number of parameters in the function
        num_params = len(node.args.args) + len(node.args.kwonlyargs)
        if node.args.vararg:
            num_params += 1
        if node.args.kwarg:
            num_params += 1
        self.function_parameter_count.append(num_params)

        # Continue visiting child nodes
        self.generic_visit(node)

        # After visiting all child nodes, store metrics for the function
        self.function_has_nested_loop.append(self.has_nested_loop)
        self.function_cyclomatic_complexity.append(self.cyclomatic_complexity)

def analyze_functions(directory):
    function_details = []
    todos = []
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(foldername, filename)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    file_content = file.read()
                    tree = ast.parse(file_content, filename=file_path)
                    function_visitor = FunctionVisitor()
                    function_visitor.visit(tree)
                    for lineno, line in enumerate(file_content.splitlines(), start=1):
                        if "TODO" in line:
                            todos.append((file_path, lineno, line.strip()))
                    for func_name, line_count, has_nested_loop, cyclomatic_complexity, num_params in zip(
                            function_visitor.function_names, function_visitor.function_line_counts,
                            function_visitor.function_has_nested_loop, function_visitor.function_cyclomatic_complexity,
                            function_visitor.function_parameter_count):
                        function_details.append((file_path, func_name, line_count, has_nested_loop, cyclomatic_complexity, num_params))
    return function_details, todos

def main():
    directory_absolut_path = 'C:\\Your_project\\root\\src'
    function_details, todos = analyze_functions(directory_absolut_path)

    # subring which is removed before printing to console in order to save space
    directory_absolut_path_substring_to_remove = "C:\\Your_project\\"

    lines_of_code = []
    nested_loops = []
    funct_cyclomatic_complexity = []
    funct_parameter_count = []

    for file_path, func_name, line_count, has_nested_loop, cyclomatic_complexity, num_params in function_details:
        if line_count > 30:
            lines_of_code.append(f'{file_path} - {func_name}: {line_count} lines')
        if has_nested_loop:
            nested_loops.append(f'{file_path} - {func_name} has a nested loop')
        if cyclomatic_complexity > 5:
            funct_cyclomatic_complexity.append(f'{file_path} - {func_name} has a cyclomatic complexity of {cyclomatic_complexity}')
        if num_params > 3:
            funct_parameter_count.append(f'{file_path} - {func_name} has {num_params} parameters')

    print("Functions with more than 30 lines of code:")
    for loc in lines_of_code:
        print(loc.replace(directory_absolut_path_substring_to_remove, ""))

    print("\nFunctions with nested loops:")
    for nl in nested_loops:
        print(nl.replace(directory_absolut_path_substring_to_remove, ""))

    print("\nFunctions cyclomatic complexity:")
    for cc in funct_cyclomatic_complexity:
        print(cc.replace(directory_absolut_path_substring_to_remove, ""))

    print("\nFunction parameter count:")
    for pc in funct_parameter_count:
        print(pc.replace(directory_absolut_path_substring_to_remove, ""))

    print("\nTODOs:")
    for file_path, lineno, comment in todos:
        print(f"{file_path.replace(directory_absolut_path_substring_to_remove, '')}: Line {lineno}: {comment}")

if __name__ == "__main__":
    main()
