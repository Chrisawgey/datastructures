def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = [None] * len(expression)
    stack_top = -1
    postfix = ''

    for char in expression:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack_top += 1
            stack[stack_top] = char
        elif char == ')':
            while stack[stack_top] != '(':
                postfix += stack[stack_top]
                stack_top -= 1
            stack_top -= 1
        else:
            while stack_top != -1 and precedence(char) <= precedence(stack[stack_top]):
                postfix += stack[stack_top]
                stack_top -= 1
            stack_top += 1
            stack[stack_top] = char

    while stack_top != -1:
        postfix += stack[stack_top]
        stack_top -= 1

    return postfix

expression = "a+b*(c^d-e)^(f+g*h)-i"
print("Infix Expression:", expression)
print("Postfix Expression:", infix_to_postfix(expression))
