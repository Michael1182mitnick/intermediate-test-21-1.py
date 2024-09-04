# Create a basic calculator that can evaluate simple arithmetic expressions (e.g., "3 + 5 / 2").
# This solution will handle addition (+), subtraction (-), multiplication (*), and division (/), respecting operator precedence and left-to-right evaluation.

def calculate(expression):
    """
    Evaluates a simple arithmetic expression containing +, -, *, /.
    Supports integer and floating-point division.
    """
    def evaluate(tokens):
        stack = []
        num = 0
        sign = "+"
        i = 0

        while i < len(tokens):
            token = tokens[i]

            if token.isdigit():
                num = int(token)
            elif token == '(':
                # Evaluate expression inside parentheses
                j = i
                parentheses_count = 0
                while i < len(tokens):
                    if tokens[i] == '(':
                        parentheses_count += 1
                    elif tokens[i] == ')':
                        parentheses_count -= 1
                    if parentheses_count == 0:
                        break
                    i += 1
                num = evaluate(tokens[j + 1:i])
            if token in "+-*/)" or i == len(tokens) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    # Integer division that truncates towards zero
                    stack.append(int(stack.pop() / num))
                sign = token
                num = 0
            i += 1

        return sum(stack)

    # Remove spaces and handle empty expressions
    expression = expression.replace(' ', '')
    if not expression:
        return 0

    # Convert the string expression into a list of tokens (numbers and operators)
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            num = ''
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            tokens.append(num)
        else:
            tokens.append(expression[i])
            i += 1

    # Evaluate the tokens and return the result
    return evaluate(tokens)


# Example usage
expression = "3 + 5 / 2"
print(f"Result of '{expression}' is: {calculate(expression)}")  # Output: 5

expression = "2 * (3 + 5) - 8 / 4"
print(f"Result of '{expression}' is: {calculate(expression)}")  # Output: 14
