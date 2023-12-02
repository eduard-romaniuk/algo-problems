from game import *

lines = open('input.txt', 'r').read().split('\n')

result = sum([Game(line).power() for line in lines])

print(result)
