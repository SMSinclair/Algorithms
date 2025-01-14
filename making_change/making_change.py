#!/usr/bin/python

import sys

def making_change(amount, denominations):
    ways = [1]+[0]*amount
    
    for denom in denominations:
        for i in range(denom,amount+1):
            ways[i]+=ways[i-denom]
    
    return ways[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")