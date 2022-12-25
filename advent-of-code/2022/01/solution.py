result = []

for group in open('input.txt', 'r').read().split('\n\n'):
    group_sum = 0
    for line in group.split('\n'):
        group_sum += int(line)
    result.append(group_sum)

result.sort(reverse=True)

print('Task 1:', result[0])
print('Task 2:', sum(result[:3]))
