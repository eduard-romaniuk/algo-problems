from game import *

lines = open('input.txt', 'r').read().split('\n')

result = 0
for line in lines:
    game = Game(line)
    if game.is_qualified():
        result += game.id

print(result)
