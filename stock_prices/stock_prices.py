#!/usr/bin/python

import argparse
import os

os.system('clear')

'''
RUN-TIME COMPLEXITY: O(n)

Justification: 
    The first loop runs N-1 times. 
    Drop the constant and you get O(n).
    The second loop runs N-k times, where k is the sell index.
    In a worst case scenario, k is the last index of the array
        leaving us with N-1 again.
    Drop the constant and you O(n).
    Adding the two constants together you get
        O(n + n) or O(2n)
    Drop the constants one last time and you get O(n)

'''


def find_max_profit(prices):
    sell = 0
    largest = prices[1]
    # find the largest price in the list --> set the index to sell
    # beginning at one as their has to be one buy available before
    # sell
    for i in range(1, len(prices)):
        if prices[i] >= largest:
            largest = prices[i]
            sell = i

    buy = 0
    smallest = prices[0]
    # find the lowest price in the list *up to sell* and set that to buy
    for j in range(0, sell):
        if prices[j] <= smallest:
            smallest = prices[j]
            buy = j
    # return the difference
    return prices[sell] - prices[buy]


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
