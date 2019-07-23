x = input('Введите выражение: ')
tokens = []
while True:
    for i, ch in enumerate(x):
        if ch in ('+', '-', '*', '/'):
            tokens.append(float(x[:i]))
            tokens.append(x[i])
            x = x[i+1:]
            break
    else:
        tokens.append(float(x))
        break
for i in range(len(tokens) -1, 0, -1):
    token = tokens[i]
    if token == '*':
        tokens[i-1] = tokens[i-1] * tokens[i+1]
        del tokens[i:i+2]
    elif token == '/':
        tokens[i-1] = tokens[i-1] / tokens[i+1]
        del tokens[i:i+2]
for i in range(len(tokens) -1, 0, -1):
    token = tokens[i]
    if token == '+':
        tokens[i-1] = tokens[i-1] + tokens[i+1]
        del tokens[i:i+2]
    elif token == '-':
        tokens[i-1] = tokens[i-1] - tokens[i+1]
        del tokens[i:i+2]
assert len(tokens) == 1
print(*tokens)