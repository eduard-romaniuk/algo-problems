monkeys = {}

lines = open('input.txt', 'r').read().split('\n')

for line in lines:
    name, expr = line.split(": ")
    if expr.isnumeric():
        monkeys[name] = int(expr)
        continue
    left, op, right = expr.split()
    if left not in monkeys or right not in monkeys:
        lines.append(line)
        continue
    monkeys[name] = eval(f'{monkeys[left]} {op} {monkeys[right]}')

print(int(monkeys['root']))
