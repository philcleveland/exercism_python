import math


def classify(number):
    if number < 1:
        raise ValueError(".+")
    # this edge case is awkward.
    # seems like 1 should be perfect
    if number == 1:
        return "deficient"

    a = aliquotSum(number)
    if a == number:
        return "perfect"
    elif a > number:
        return "abundant"
    else:
        return "deficient"

def aliquotSum(number):
    result = {1}
    start = math.floor(number / 2)
    for i in range(start, 1, -1):
        if number % i == 0:
            result.add(i)
    return sum(result)
