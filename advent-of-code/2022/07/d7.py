from system import *

lines = open('input.txt', 'r').read().split('\n')

currentDir = Dir('/')
root = currentDir

for line in lines[1:]:
    if line == '$ ls':
        continue
    if line.startswith('$ cd '):
        currentDir = currentDir.get_dir(line[5:])
        continue
    if line.startswith('dir '):
        currentDir.add_dir(Dir(line[4:], currentDir))
        continue
    file = line.split(' ')
    currentDir.add_file(File(file[1], int(file[0])))

dirs_sizes = sizes(root)

result1 = sum(filter(lambda size: size <= 100000, dirs_sizes))
print(f'Task 1: {result1}')  # 1642503

need = root.size + 30000000 - 70000000
result2 = min(filter(lambda size: size > need, dirs_sizes))
print(f'Task 2: {result2}')  # 6999588
