def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():  # Check if the token is an operand (number)
            stack.append(int(token))
        else:
            # The token is an operator, so pop two operands from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Apply the operator
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            else:
                raise ValueError(f"Unsupported operator: {token}")

            # Push the result back into stack
            stack.append(result)

    # The final result is at the top of the stack
    return stack.pop()

expression = "3 4 + 2 * 7 /"  # This represents the postfix expression (3 + 4) * 2 / 7
result = evaluate_postfix(expression)
print("Result:", result)

