"""
Advent of Code - Day 4

Camp Cleanup

cleanup section assignments overlap

In how many assignment pairs does one range fully contain the other?
ie 2-8 fully contains 3-7
"""

import pandas as pd

cleanup = pd.read_csv('input.txt', sep=',', header=None, names=['elf1', 'elf2'])

cleanup.head()

elf1 = [tuple(map(int, i.split('-'))) for i in cleanup['elf1']]
elf2 = [tuple(map(int, i.split('-'))) for i in cleanup['elf2']]

fully_contained = 0
for idx, i in enumerate(elf1):
    if (i[0] <= elf2[idx][0] and i[1] >= elf2[idx][1]) or \
        (i[0] >= elf2[idx][0] and i[1] <= elf2[idx][1]):
            fully_contained += 1
            
print(fully_contained)

"""
PART 2
count assignment pairs that overlap at all
"""

overlap = 0
for idx, i in enumerate(elf1):
    if elf2[idx][0] in range(i[0], i[1]+1) or \
       elf2[idx][1] in range(i[0], i[1]+1) or \
       i[0] in range(elf2[idx][0], elf2[idx][1]+1) or \
       i[1] in range(elf2[idx][0], elf2[idx][1]+1):
           overlap += 1
            
print(overlap)     