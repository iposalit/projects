"""
Advent of Code - Day 5

Supply Stacks

After the rearrangement procedure completes, what crate ends up on top of each stack?

"""
file1 = open('input.txt', 'r')
# readlines() method returns a list containing each line in the file as a list item.
lines = file1.readlines()
data = [entry.strip('\n') for entry in lines]

stacks = data[0:data.index('')]
steps = data[data.index('') + 1:]

boxes_to_move = [int(x.split(' ')[1]) for x in steps]
from_stack = [int(x.split(' ')[3]) for x in steps]
to_stack = [int(x.split(' ')[5]) for x in steps]
         

stacks

# rearrange input into a dictionary of numbered stacks
new_stacks = {}
for i in range(1, 10):
    new_stacks[i] = []
        
    for j in range(7, -1, -1):
        idx = (i - 1) * 3 + i
        if stacks[j][idx].isalnum():
            new_stacks[i].append(stacks[j][idx])

new_stacks

# using pop and append, move the crates
for i in range(len(steps)):    
    for n in range(boxes_to_move[i]):
        new_stacks[to_stack[i]].append(new_stacks[from_stack[i]].pop())

# get the top crate (last letter) of each stack        
message = ''        
for i in range(1, 10):
    message += new_stacks[i][-1]

print(message)

"""
PART 2

crates don't follow LIFO rule of stacks, can be moved while maintaining their order
"""

# rearrange input into a dictionary of numbered stacks
new_stacks = {}
for i in range(1, 10):
    new_stacks[i] = []
        
    for j in range(7, -1, -1):
        idx = (i - 1) * 3 + i
        if stacks[j][idx].isalnum():
            new_stacks[i].append(stacks[j][idx])

# move the crates in aggregate for each step using slicing
for i in range(len(steps)):
    n = boxes_to_move[i]
    ls = new_stacks[from_stack[i]]
    
    # append crates to to_stack
    new_stacks[to_stack[i]].extend(ls[len(ls) - n:])
    # remove from from_stack
    del new_stacks[from_stack[i]][len(ls) - n:]

# get the top crate (last letter) of each stack        
message = ''        
for i in range(1, 10):
    message += new_stacks[i][-1]

print(message)
