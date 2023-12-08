import re

route_regex = re.compile(r'[A-Z]{3}')
instructions, routes_desc = open('input.txt', 'r').read().split('\n\n')
routes = {}
for route in routes_desc.split('\n'):
    vals = route_regex.findall(route)
    routes[vals[0]] = (vals[1], vals[2])


i = 0
steps = 0
current_route = 'AAA'
while current_route != 'ZZZ':
    direction = 0 if instructions[i] == 'L' else 1
    current_route = routes[current_route][direction]
    i = (i + 1) % len(instructions)
    steps += 1

print('Result:', steps)
