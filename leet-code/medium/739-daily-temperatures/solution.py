# Time O(n)
# Space O(n)
def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            cur = stack.pop()
            result[cur] = i - cur
        stack.append(i)
    return result
