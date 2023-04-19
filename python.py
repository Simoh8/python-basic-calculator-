import ast
import operator

# Define a dictionary to store variables and their values
variables = {}

# Define a dictionary of supported operators
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}

def evaluate_expression(expression):
    # Evaluate a mathematical expression
    node = ast.parse(expression.replace('^', '**'), mode='eval').body

    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Name):
            return variables[node.id]
        elif isinstance(node, ast.BinOp):
            return operators[type(node.op)](_eval(node.left), _eval(node.right))
        else:
            raise TypeError(node)

    return _eval(node)

def main():
    # Read input from the user
    print("Add expressions (type 'quit' to exit):")
    while True:
        input_string = input("> ")
        if input_string == "quit":
            break

        # Parse the input and evaluate the expressions
        if "=" in input_string:
            variable, expression = map(str.strip, input_string.split("=", 1))
            variables[variable] = evaluate_expression(expression)
        elif "print" in input_string:
            variables_to_print = map(str.strip, input_string.split("print")[1].split(","))
            values_to_print = [str(variables[variable]) for variable in variables_to_print]
            print(" ".join(values_to_print))
        else:
            result = evaluate_expression(input_string)
            print("{:.1f}".format(result))

    # Print the final variable values
    print(variables)

if _name_ == "_main_":
    main()