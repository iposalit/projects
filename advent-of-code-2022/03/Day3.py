"""
Advent of Code - Day 3

Rucksack Reorganization

rucksack has: vJrwpWtwJgWrhcsFMMfFFhFp
first compartment = vJrwpWtwJgWr
second compartment = hcsFMMfFFhFp
common item type = 'p'

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.

'p' priority = 16

Find the item type that appears in both compartments of each rucksack. 
What is the sum of the priorities of those item types?
"""
import pandas as pd

df = pd.read_csv('input.txt', sep=' ', header=None, names=["rucksacks"])
rucksacks = df['rucksacks']

import string

alphabet = list(string.ascii_letters)
priority_sum = 0

for i in rucksacks:
    half = int(len(i)/2)
    first_set = set(i[:half])
    second_set = set(i[half:])
    odd_item_out = min(first_set & second_set) # intersection of two sets
    
    priority_sum += (alphabet.index(odd_item_out) + 1)

print(priority_sum)

"""
PART 2
every three lines (three rucksacks) is one group of three elves
find the item common among the three
get the priority 
sum the priorities of all groups
"""
priority_sum = 0
for i in range(0, len(rucksacks), 3):
    common_item = min(set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2]))
    priority_sum += (alphabet.index(common_item) + 1)

print(priority_sum)  

