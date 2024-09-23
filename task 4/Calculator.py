def evaluate_term(expr, index):
    """Evaluate a term which can be a number or an expression in parentheses."""
    num = 0
    while index < len(expr) and expr[index].isdigit():
        num = num * 10 + int(expr[index])
        index += 1
    return num, index

def evaluate_expression(expr, index):
    """Evaluate the expression and return the result along with the new index."""
    stack = []
    sign = 1  # 1 for '+', -1 for '-'
    
    while index < len(expr):
        char = expr[index]

        if char.isdigit():
            num, index = evaluate_term(expr, index)
            stack.append(sign * num)

        elif char == '+':
            sign = 1
            index += 1
        elif char == '-':
            sign = -1
            index += 1
        elif char == '(':
            num, index = evaluate_expression(expr, index + 1)
            stack.append(sign * num)
        elif char == ')':
            return sum(stack), index + 1
        elif char in '*/':
            index += 1
            num, index = evaluate_term(expr, index)
            if char == '*':
                stack[-1] *= num
            elif char == '/':
                if num != 0:
                    stack[-1] //= num
                else:
                    return "Error: Division by zero.", index

    return sum(stack), index

def parse_expression(expression):
    """Main function to parse and evaluate the input expression."""
    result, _ = evaluate_expression(expression, 0)
    return result

# User interaction
print("Simple Calculator")
print("Enter a mathematical expression using integers and operators (+, -, *, /).")

expression = input("Enter expression: ")
expression = expression.replace(" ", "")  # Remove spaces
print(f"Expression: {expression}")

result = parse_expression(expression)
print(f"Result: {result}")
