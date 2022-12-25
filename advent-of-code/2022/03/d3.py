import string

alphabet = {l: i + 1 for i, l in enumerate(list(string.ascii_lowercase + string.ascii_uppercase))}
lines = open('input.txt', 'r').read().splitlines()

# Task 1

result = 0

for line in lines:
    center = len(line) // 2
    c2 = line[center:]
    for char in line[:center]:
        if char in c2:
            result += alphabet[char]
            break

print('Task 1:', result)

# Task 2

result = 0
groups_count = len(lines) // 3

for i in range(groups_count):
    seen = {}
    for j in range(3):
        for c in set(lines[i * 3 + j]):
            seen[c] = seen.get(c, 0) + 1
            if seen[c] == 3:
                result += alphabet[c]
                break

print('Task 2:', result)
