#!/usr/bin/python3

# 35 total heads
# 94 feet
# how many rabbits and chickens

for num in range(1, 35):
    chickens = 35 - num
    rabbits = 35 - chickens
    if 4 * rabbits + 2 * chickens == 94:
        print(f'There are {rabbits} rabbits and {chickens} chickens.')
        break
