#!/usr/bin/python

import sys

def rock_paper_scissors(n):

    def rps_recursive(n):
        choices = [['rock'], ['paper'], ['scissors']]
        if n == 0:
            return [[]]
        if n == 1:
            return choices

        result = []
        for element in rps_recursive(n-1):
            for choice in choices:
                result.append(element + choice)
        return result

    return rps_recursive(n)




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

