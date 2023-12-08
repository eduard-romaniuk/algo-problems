import re
import math

route_regex = re.compile(r'[A-Z]{3}')
instructions, routes_desc = open('input.txt', 'r').read().split('\n\n')
routes = {}
for route in routes_desc.split('\n'):
    vals = route_regex.findall(route)
    routes[vals[0]] = (vals[1], vals[2])

current_routes = [route for route in routes.keys() if route[-1] == 'A']
steps_to_exit = []
for current_route in current_routes:
    i = 0
    steps = 0
    while current_route[-1] != 'Z':
        direction = 0 if instructions[i] == 'L' else 1
        current_route = routes[current_route][direction]
        i = (i + 1) % len(instructions)
        steps += 1
    steps_to_exit.append(steps)

print('Result:', math.lcm(*steps_to_exit))
