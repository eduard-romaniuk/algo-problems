def solution(data: list[int], rounds=1, decryption_key=1) -> (list[int], int):
    data = [n * decryption_key for n in data]
    _len = len(data)

    def normalize_index(i):
        if abs(i) < _len:
            return i
        if i > 0:
            return i % (_len - 1)
        return -(-i % (_len - 1))

    result = list(enumerate(data))

    for _ in range(rounds):
        for shift in enumerate(data):
            _index = 0
            for index, item in enumerate(result):
                if shift == item:
                    _index = index
                    break
            new_index = normalize_index(_index + shift[1])
            del result[_index]
            result.insert(new_index, shift)

    zero_index = 0
    for index, item in enumerate(result):
        if item[1] == 0:
            zero_index = index
            break

    total = sum([result[(zero_index + i) % _len][1] for i in [1000, 2000, 3000]])

    return total


if __name__ == '__main__':
    INPUT_DATA = [int(i) for i in open('input.txt', 'r').read().split('\n')]
    print('Task 1:', solution(INPUT_DATA))
    DECRYPTION_KEY = 811589153
    ROUNDS = 10
    print('Task 2:', solution(INPUT_DATA, decryption_key=DECRYPTION_KEY, rounds=ROUNDS))
