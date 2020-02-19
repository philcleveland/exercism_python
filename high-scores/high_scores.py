# mutating the passed in array feels wrong but it's more
# efficient than copying the arr and the tests pass
def latest(scores):
    return scores[-1]


def personal_best(scores):
    scores.sort()
    return scores[-1]


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[:3]
