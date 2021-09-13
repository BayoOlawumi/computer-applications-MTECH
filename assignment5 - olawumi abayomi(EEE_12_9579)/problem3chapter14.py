"""Adapt the queens program so that we keep a list of solutions that have already printed, so that
we don’t print the same solution more than once."""

import time


def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)  # Calc the absolute y distance
    dx = abs(x1 - x0)  # CXalc the absolute x distance
    return dx == dy  # They clash if dx == dy


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):  # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True

    return False  # No clashes - col c has a safe placement.


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


t0 = 0
t = 0


def queen_generator(size):
    import random
    rng = random.Random()  # Instantiate a generator
    bd = list(range(size))  # Generate the initial permutation
    tries = 0
    numfound= 0
    start_time = time.perf_counter()
    generated = []
    while True:
        rng.shuffle(bd)
        tries += 1
        time_diff = time.perf_counter() - start_time
        if time_diff >= 60:
            print("We could only solve {0} puzzles in 1 minute when N is {1}".format(numfound,size))
            break
        if not has_clashes(bd):
            if bd in generated:
                continue
            else:
                print("Found solution {0} in {1} tries.".format(bd, tries))
                tries = 0
                numfound += 1
                generated.append(bd)
    print(generated)


print("*******************When n is 12**************************")
n= 12
queen_generator(n)
