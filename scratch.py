def calculate(expression):
    stack = []

    def perform_operation(op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return int(a / b)
        elif op == '~':
            return -a
        elif op == '!':
            return 1 if a == 0 else a * calculate(f"{a} ! - 1 +")

    for token in expression:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(int(token))
        elif token in {'+', '-', '*', '/', '~'}:
            if len(stack) >= 2:
                b, a = stack.pop(), stack.pop()
                stack.append(perform_operation(token, a, b))
        elif token == '!':
            if len(stack) >= 1:
                stack[-1] = perform_operation(token, stack[-1], 0)
        elif token == '#':
            if len(stack) >= 1:
                stack.append(stack[-1])
        elif token == '@':
            if len(stack) >= 3:
                c, b, a = stack.pop(), stack.pop(), stack.pop()
                stack.extend([b, c, a])
        print(stack, token)
    return stack[0]


# Ввод данных
expression = input().split()

# Выполнение с введенным выражением
result = calculate(expression)
print(result)
