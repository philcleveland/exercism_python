"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12


def score(dice, category):
    if len(dice) != 5:
        raise ValueError

    if category == YACHT:
        s = set(dice)
        return 50 if len(s) == 1 else 0

    elif category == ONES or category == TWOS or category == THREES or \
            category == FOURS or category == FIVES or category == SIXES:
        return calcBasic(dice, category)

    elif category == FULL_HOUSE:
        s = sorted(set(dice))
        l = len(s)

        if l != 2:
            return 0

        val = 0
        for i in s:
            if dice.count(i) == 1 or dice.count(i) == 4:
                return 0
            else:
                val += i * dice.count(i)
        return val

    elif category == FOUR_OF_A_KIND:

        s = set(dice)
        l = len(s)
        # yacht passed as 4 of a kind
        if l == 1:
            return s.pop() * 4
        elif l == 2:
            val = 0
            for i in s:
                if dice.count(i) == 2 or dice.count(i) == 3:
                    return 0
                elif dice.count(i) == 1:
                    continue
                else:
                    val += i * dice.count(i)
            return val
        else:
            return 0

    elif category == LITTLE_STRAIGHT:
        dice.sort()
        return 30 if dice == [1, 2, 3, 4, 5] else 0
    elif category == BIG_STRAIGHT:
        dice.sort()
        return 30 if dice == [2, 3, 4, 5, 6] else 0
    elif category == CHOICE:
        return sum(dice)
    else:
        raise("Invalid category")


def calcBasic(dice, num):
    val = 0
    for i in dice:
        if i == num:
            val += num
    return val
