import re

stack_init, instructions_init = [part.splitlines() for part in open('input.txt', 'r').read().split('\n\n')]

stack_length = int(stack_init[-1].strip()[-1])
stack_init = list(reversed(stack_init[:-1]))
stacks = [[] for i in range(stack_length)]

NUMBER = re.compile(r'\d+')
instructions = [tuple(map(int, NUMBER.findall(line))) for line in instructions_init]

for row in stack_init:
    for stack_index in range(stack_length):
        val = row[stack_index * 4 + 1]
        if val != ' ':
            stacks[stack_index].append(val)


def solution(is_first):
    local_stacks = [[box for box in stack] for stack in stacks]
    for count, from_stack, to_stack in instructions:
        boxes = local_stacks[from_stack - 1][-count:]
        if is_first:
            boxes.reverse()
        local_stacks[to_stack - 1].extend(boxes)
        del local_stacks[from_stack - 1][-count:]
    return ''.join([i[-1] for i in local_stacks])


print(f'Task 1: {solution(True)}')
print(f'Task 2: {solution(False)}')
