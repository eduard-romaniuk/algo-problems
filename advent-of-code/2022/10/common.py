def read_commands():
    commands = []
    for line in open('input.txt', 'r').read().splitlines():
        if 'addx' in line:
            commands.append('addx 0')
        commands.append(line)
    return commands
