import random
import sys


class Empty(Exception):
    pass

def randomInt(low, high):
    if low > high:
        low, high = high, low
    return random.randint(low, high)

def randomRange(range = sys.maxint):
    return randomInt(0, range)

def flipCoin():
    return randomInt(0, sys.maxint) > sys.maxint / 2

def clamp(val, min, max):
    if val < min:
        return min
    elif val > max:
        return max
    else:
        return val

class NodeType(object):

    Root = 0
    LC = 1
    RC = -1

if __name__ == '__main__':
    print random.randint(0, 3)