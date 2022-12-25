def to_range(section_assignment):
    start, end = section_assignment.split('-')
    return set(range(int(start), int(end) + 1))


lines = open('input.txt', 'r').read().splitlines()
result1 = 0
result2 = 0

for line in lines:
    elf1, elf2 = tuple(sorted(map(to_range, line.split(',')), key=len))
    if all(x in elf2 for x in elf1):
        result1 += 1
    if len(elf1.intersection(elf2)) > 0:
        result2 += 1

print('Task 1:', result1)
print('Task 2:', result2)
