#!/usr/bin/python

import sys
import os

os.system("clear")

'''
    This is a WIP:

    If the end result is the following for n = 2:

            ['rock', 'rock'],
            ['rock', 'paper'],
            ['rock', 'scissors'],
            ['paper', 'rock'],
            ['paper', 'paper'],
            ['paper', 'scissors'],
            ['scissors', 'rock'],
            ['scissors', 'paper'],
            ['scissors', 'scissors']

    What the function is doing is returning all the index[0]'s
    for the set of permutations.

    So input n = 1 would give you:

        ['rock', 'paper', 'scissors']

    Input n = 2 would give you:

        ['rock', 'rock', 'rock', 'paper', 'paper', 'paper', 'scissors', 
        'scissors', 'scissors']


    If I start with input n, I'll have the set of index[0]'s
    for all the permutations

    n-1, I'll have the set of index[1]'s

    n-2, I'll have the set of index[2]'s

    So on, so forth... but I need a way to "glue" them altogether in
    the helper function

    This is probably so much more complicated than it needs to be, but I tried.

'''

rps = ['rock', 'paper', 'scissors']


def create_perm(n):
    player = n-1
    num_plays = len(rps)
    num_perms = num_plays**n
    next_arr = [0] * num_perms * 1

    for i in range(num_perms):
        play = i % num_perms // num_plays**(n-1)
        next_arr[i] = rps[play]

    return next_arr


def rock_paper_scissors(n):
    return create_perm(n)


result = rock_paper_scissors(2)
print(result)


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays = int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print('Usage: rps.py [num_plays]')
