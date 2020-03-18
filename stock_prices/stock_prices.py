#!/usr/bin/python

import argparse
import os

os.system('clear')


def find_max_profit(prices):

    sell = 0
    largest = prices[1]
    for i in range(1, len(prices)):
        if prices[i] >= largest:
            largest = prices[i]
            sell = i

    buy = 0
    smallest = prices[0]
    for j in range(0, sell):
        if prices[j] <= smallest:
            smallest = prices[j]
            buy = j

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
