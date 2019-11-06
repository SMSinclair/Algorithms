#!/usr/bin/python

import argparse

def find_max_profit(prices):
    if len(prices) < 2:
        return "prices must contain two or more integers"
    max_profit = prices[1] - prices[0]
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit
print(find_max_profit([10, 7, 5, 8, 11, 9]))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))