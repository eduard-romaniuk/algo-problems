import tests


# Time O(n)
# Space O(n)
def min_rewards(scores):
    rewards = [1] * len(scores)
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)


tests.test(min_rewards)
