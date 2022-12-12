import sys
import numpy as np
from collections import defaultdict, Counter, deque
from pathlib import Path
from timeit import default_timer as timer
import re


def timer_func(func):
    # This function shows the execution time of the function object passed
    def wrap_func(*args, **kwargs):
        t1 = timer()
        result = func(*args, **kwargs)
        t2 = timer()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        total_time.append((t2 - t1))
        return result
    return wrap_func


@timer_func
def get_data(inputdata):
    infile = sys.argv[1] if len(sys.argv) > 1 else inputdata
    parsed = []
    starting = []
#    operation = []
    test = []
    test_true = []
    test_false = []
    with open(infile, 'r') as f:
        for group in f.read().split('\n\n'):
            inputs = group.split('\n')
            starting = (re.findall(r'\d+', inputs[1]))
#            operation.append(re.findall(r'\d+', inputs[2]))
            test = (re.findall(r'\d+', inputs[3]))
            test_true = (re.findall(r'\d+', inputs[4]))
            test_false = (re.findall(r'\d+', inputs[5]))
            parsed.append([starting, test, test_true, test_false])
    return parsed


@timer_func
def part_one(inputlist):
    """
    1.   Input is
    Monkey a:
        Starting items: s1, s2
        Operation: new = old * 19
        Relief: divide by 3 and round down
        Test: divisible by 23
            If true: throw to monkey b
            If false: throw to monkey c

    :param inputlist:
    :return:
    """
    starting = [[74, 64, 74, 63, 53],
                [69, 99, 95, 62],
                [59, 81],
                [50, 67, 63, 57, 63, 83, 97],
                [61, 94, 85, 52, 81, 90, 94, 70],
                [69],
                [54, 55, 58],
                [79, 51, 83, 88, 93, 76]]

    test = [5, 17, 7, 13, 19, 3, 11, 2]

    test_true = [1, 2, 4, 0, 7, 4, 1, 0]

    test_false = [6, 5, 3, 7, 3, 2, 5, 6]

    handled = [0, 0, 0, 0, 0, 0, 0, 0]


#    starting = [[79, 98],
#                [54, 65, 75, 74],
#                [79, 60, 97],
#                [74]]

#    test = [23, 19, 13, 17]

#    test_true = [2, 2, 1, 0]

#    test_false = [3, 0, 3, 1]

#    handled = [0, 0, 0, 0]

    for round in range(1, 21):
        DEBUG1 and print(f"\n\nRound: {round}")
        for monkey, items in enumerate(starting):
            num = len(items)
            DEBUG1 and print(f"\tMonkey: {monkey}, num: {num}")
            for old in items:
                if monkey == 0:
                    new = old * 7
                elif monkey == 1:
                    new = old * old
                elif monkey == 2:
                    new = old + 8
                elif monkey == 3:
                    new = old + 4
                elif monkey == 4:
                    new = old + 4
                elif monkey == 5:
                    new = old + 5
                elif monkey == 6:
                    new = old + 7
                else:
                    new = old * 3

#                if monkey == 0:
#                    new = old * 19
#                elif monkey == 1:
#                    new = old + 6
#                elif monkey == 2:
#                    new = old * old
#                else:
#                   new = old + 3
                DEBUG1 and print(f"\t\tMonkey inspects an item with a worry level of {old}")
                DEBUG1 and print(f"\t\t\tWorry level is changed to {new}")
                new = new // 3
                DEBUG1 and print(f"\t\t\tMonkey gets bored with item. Worry level is divided by 3 to {new}")
                if new % test[monkey] == 0:
                    starting[test_true[monkey]].append(new)
                    DEBUG1 and print(f"\t\t\tCurrent worry level is divisible by {test[monkey]}.")
                    DEBUG1 and print(f"\t\t\tItem with worry level {new} is thrown to Monkey {test_true[monkey]}")
                else:
                    starting[test_false[monkey]].append(new)
                    DEBUG1 and print(f"\t\t\tCurrent worry level is not divisible by {test[monkey]}.")
                    DEBUG1 and print(f"\t\t\tItem with worry level {new} is thrown to Monkey {test_false[monkey]}")
            starting[monkey] = []
            handled[monkey] += num
            DEBUG1 and print(f"\tTotal handled: {handled[monkey]}")
    handled.sort(reverse=True)
    return handled[0] * handled[1]


@timer_func
def part_two(inputlist):
    """
    1.   Input is
    Monkey a:
        Starting items: s1, s2
        Operation: new = old * 19
        Relief: divide by 3 and round down
        Test: divisible by 23
            If true: throw to monkey b
            If false: throw to monkey c

    :param inputlist:
    :return:
    """
    starting = [[74, 64, 74, 63, 53],
                [69, 99, 95, 62],
                [59, 81],
                [50, 67, 63, 57, 63, 83, 97],
                [61, 94, 85, 52, 81, 90, 94, 70],
                [69],
                [54, 55, 58],
                [79, 51, 83, 88, 93, 76]]

    test = [5, 17, 7, 13, 19, 3, 11, 2]

    test_true = [1, 2, 4, 0, 7, 4, 1, 0]

    test_false = [6, 5, 3, 7, 3, 2, 5, 6]

    handled = [0, 0, 0, 0, 0, 0, 0, 0]

    lcd = 5*17*7*13*19*3*11*2

#    starting = [[79, 98],
#                [54, 65, 75, 74],
#                [79, 60, 97],
#                [74]]

#    test = [23, 19, 13, 17]

#    test_true = [2, 2, 1, 0]

#    test_false = [3, 0, 3, 1]

#    handled = [0, 0, 0, 0]

#    lcd = 23*19*13*17

    for round in range(1, 10000+1):
        DEBUG2 and print(f"\n\nRound: {round}")
        for monkey, items in enumerate(starting):
            num = len(items)
            DEBUG2 and print(f"\tMonkey: {monkey}, num: {num}")
            for old in items:
                if monkey == 0:
                    new = old * 7
                elif monkey == 1:
                    new = old * old
                elif monkey == 2:
                    new = old + 8
                elif monkey == 3:
                    new = old + 4
                elif monkey == 4:
                    new = old + 3
                elif monkey == 5:
                    new = old + 5
                elif monkey == 6:
                    new = old + 7
                else:
                    new = old * 3

#                if monkey == 0:
#                    new = old * 19
#                elif monkey == 1:
#                    new = old + 6
#                elif monkey == 2:
#                    new = old * old
#                else:
#                   new = old + 3

                DEBUG2 and print(f"\t\tMonkey inspects an item with a worry level of {old}")
                DEBUG2 and print(f"\t\t\tWorry level is changed to {new}")
#                new = int(new / 3)
                new = new // 1 % lcd
                DEBUG2 and print(f"\t\t\tMonkey gets bored with item. Worry level is divided by 3 to {new}")
                if new % test[monkey] == 0:
                    starting[test_true[monkey]].append(new)
                    DEBUG2 and print(f"\t\t\tCurrent worry level is divisible by {test[monkey]}.")
                    DEBUG2 and print(f"\t\t\tItem with worry level {new} is thrown to Monkey {test_true[monkey]}")
                else:
                    starting[test_false[monkey]].append(new)
                    DEBUG2 and print(f"\t\t\tCurrent worry level is not divisible by {test[monkey]}.")
                    DEBUG2 and print(f"\t\t\tItem with worry level {new} is thrown to Monkey {test_false[monkey]}")
            starting[monkey] = []
            handled[monkey] += num
            DEBUG2 and print(f"\tTotal handled: {handled[monkey]}")
    handled.sort(reverse=True)
    return handled[0] * handled[1]


total_time = []
DEBUG0 = False
DEBUG1 = False
DEBUG2 = False
TESTING = False

if TESTING:
    inputData = f'{Path(__file__).stem}_test.in'
else:
    inputData = f'{Path(__file__).stem}.in'

print(f"ADVENT OF CODE: {Path(__file__).stem}")
L = get_data(inputData)
print(f"Part one: {part_one(L)}")
print(f"Part two: {part_two(L)}")
print(f"Elapsed Total time: {sum(total_time):.4f}s")
