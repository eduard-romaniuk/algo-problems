datastream = open('input.txt', 'r').read()


def solution(marker_length):
    for i in range(len(datastream) - marker_length):
        if len(set(datastream[i:i + marker_length])) == marker_length:
            return i + marker_length


print(f"Task 1: {solution(4)}")
print(f"Task 2: {solution(14)}")
