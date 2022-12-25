from common import read_commands

offset = 20
cycle = 1 + offset
signals = {}
register = 1

for command in read_commands():
    if cycle % 40 == 0:
        signals[cycle - offset] = register
    if cycle == 220 + offset:
        break
    if 'addx' in command:
        register += int(command.split(' ')[1])
    cycle += 1

print('Task 1:', sum([cycle * signal for cycle, signal in signals.items()]))
