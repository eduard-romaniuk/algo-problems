class Rope:
    moves = {
        'U': (1, 0),
        'D': (-1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }

    def __init__(self, size):
        self.tail_visited = set()
        self.rope = [(0, 0) for _ in range(size)]
        self._trace_tail()

    def move(self, direction, steps):
        for _ in range(steps):
            self._move(self.moves[direction])

    def tail_route_length(self):
        return len(self.tail_visited)

    def _move(self, move):
        self.rope[0] = (self.rope[0][0] + move[0], self.rope[0][1] + move[1])
        for i in range(1, len(self.rope)):
            self.rope[i] = self._move_body(self.rope[i - 1], self.rope[i])
        self._trace_tail()

    @staticmethod
    def _distance_between(a, b):
        return a[0] - b[0], a[1] - b[1]

    def _move_body(self, leader, follower):
        dx, dy = self._distance_between(leader, follower)
        if dx == 0 and abs(dy) > 1:
            return follower[0], follower[1] + dy // 2
        if dy == 0 and abs(dx) > 1:
            return follower[0] + dx // 2, follower[1]
        if abs(dx) > 1 and abs(dy) > 0 or abs(dx) > 0 and abs(dy) > 1:
            return follower[0] + dx // abs(dx), follower[1] + dy // abs(dy)
        return follower[0], follower[1]

    def _trace_tail(self):
        self.tail_visited.add(self.rope[-1])


rope2 = Rope(2)
rope10 = Rope(10)

for line in open('input.txt', 'r').read().split('\n'):
    args = line.split(' ')
    rope2.move(args[0], int(args[1]))
    rope10.move(args[0], int(args[1]))

print(f'Task 1: {rope2.tail_route_length()}')
print(f'Task 2: {rope10.tail_route_length()}')
