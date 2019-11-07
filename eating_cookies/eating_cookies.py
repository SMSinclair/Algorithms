#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if cache == None:
        cache = [0 for i in range(n+1)]

    def cookie_recursive(n):
        nonlocal cache # look for variable in outer scope
        # base cases
        if n<=1:
            cache[n] = 1
            return 1
        if n==2:
            cache[2] = 2
            return 2
        if n==3:
            cache[3] = 4
            return 4

        if cache[n]==0: # check cache, add cache[n] if not there
            cache[n] = cookie_recursive(n-1) + cookie_recursive(n-2) + cookie_recursive(n-3)
        
        return cache[n]
    
    return cookie_recursive(n)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')