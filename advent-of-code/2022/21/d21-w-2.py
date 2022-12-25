import sympy

monkeys = {'humn': sympy.Symbol('x')}
lines = open('input.txt', 'r').read().split('\n')

ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

for line in lines:
    name, expr = line.split(": ")
    if name in monkeys:
        continue
    if expr.isnumeric():
        monkeys[name] = sympy.Integer(expr)
        continue
    left, op, right = expr.split()
    if left not in monkeys or right not in monkeys:
        lines.append(line)
        continue
    if name == 'root':
        monkeys['root'] = sympy.solve(monkeys[left] - monkeys[right])[0]
        break
    monkeys[name] = ops[op](monkeys[left], monkeys[right])

print(monkeys['root'])
