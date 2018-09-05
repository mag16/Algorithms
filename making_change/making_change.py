#!/usr/bin/python

import sys

def making_change(amount, denominations):
  ways_of_making_n_cents = [0 for i in range(amount + 1)]
  ways_of_making_n_cents[0] = 1
  
  for coin in denominations:
    for higher_amount in range(coin, amount + 1):
      higher_amount_remainder = higher_amount - coin
      ways_of_making_n_cents[higher_amount] += ways_of_making_n_cents[higher_amount_remainder]
      
  return ways_of_making_n_cents[amount]

if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
