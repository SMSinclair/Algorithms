#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    ratio = [0] * len(items)
    total_size = 0
    sorted_items = sorted(items, key = lambda x: x.value/x.size, reverse=True)
    total_value = 0
    chosen = []

    for i in range(0, len(sorted_items)):
        ratio[i] = sorted_items[i].value/sorted_items[i].size
        print(sorted_items[i])

    for item in sorted_items:
        if total_size + item.size <= capacity:
            total_value += item.value
            total_size += item.size
            chosen.append(item.index)

    result = {'Chosen': sorted(chosen), 'Value': total_value, }
    return result


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')