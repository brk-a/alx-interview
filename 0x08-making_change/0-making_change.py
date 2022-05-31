#!/usr/bin/python3

'''
Given a pile of coins of different values, determine the fewest
number of coins needed to meet a given amount total.

Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have,
return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination
of coin in the list
Your solution’s runtime will be evaluated in this task
'''


def makeChange(coins, total):
    """change; change everywhere"""
    if total < 1:
        return 0
    coins.sort()
    coins.reverse()
    fewest = 0
    for coin in coins:
        if total <= 0:
            break
        buff = total // coin
        fewest += buff
        total -= (buff * coin)
    if total != 0:
        return -1
    return fewest


if __name__ == '__main__':
    makeChange = __import__('0-making_change').makeChange
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
