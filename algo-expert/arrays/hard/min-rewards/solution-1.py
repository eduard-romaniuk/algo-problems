import operator
import tests


# Time O(n)
# Space O(n)
def min_rewards(scores):
    rewards = [1] * len(scores)
    i = 0
    while i < len(scores):
        sequence_end = i
        is_descending = scores[i] > scores[i + 1] if i < len(scores) - 1 else scores[i - 1] > scores[i]
        comparison_operator = operator.gt if is_descending else operator.lt

        while sequence_end < len(scores) - 1 and \
                comparison_operator(scores[sequence_end], scores[sequence_end + 1]):
            sequence_end += 1

        if is_descending:
            reward = sequence_end - i + 1
            if i > 0 and rewards[i - 1] <= reward and scores[i - 1] > scores[i]:
                rewards[i - 1] = reward + 1
            while i <= sequence_end:
                rewards[i] = reward
                reward -= 1
                i += 1
        else:
            reward = 1
            if i > 0 and scores[i - 1] < scores[i]:
                reward = rewards[i - 1] + 1
            while i <= sequence_end:
                rewards[i] = reward
                reward += 1
                i += 1
    return sum(rewards)


tests.test(min_rewards)
