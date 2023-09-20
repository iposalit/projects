"""
Advent of Code - Day 8

Treetop Tree House

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. 
Only consider trees in the same row or column.
All trees along the perimeter are visible.

how many trees are visible from outside the grid?

"""

import numpy as np
with open("input.txt") as f:
    trees = np.array([[int(a) for a in list(a.strip())] for a in f.readlines()])    

visible_cnt = 0

for r in range(trees.shape[0]):
    row = trees[r]      
    for c in range(trees.shape[1]):
        col = trees[:, c]
        currTree = trees[r][c]
        # outer perimeter trees are all visible
        if r == 0 or r == trees.shape[0] - 1 or c == 0 or c == trees.shape[1] - 1:
            visible_cnt += 1
        else:
            if any([currTree > max(row[:c]), 
                    currTree > max(row[c + 1:]),
                    currTree > max(col[:r]),
                    currTree > max(col[r + 1:])
                    ]):
                visible_cnt += 1

print(visible_cnt)
"""
PART 2 - Scenic Score
To measure the viewing distance from a given tree, look up, down, left, and right from that tree; 
stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration.

A tree's scenic score is found by multiplying together its viewing distance in each of the four directions.
Consider each tree on your map. What is the highest scenic score possible for any tree?
"""       

maxScenicScore = 0

for r in range(trees.shape[0]):
    row = trees[r]      
    for c in range(trees.shape[1]):
        col = trees[:, c]
        currTree = trees[r][c]
        
        # outer perimeter trees score is 0 because at least one direction viewing distance is 0
        if r == 0 or r == trees.shape[0] - 1 or c == 0 or c == trees.shape[1] - 1:
            score = 0
        else:
            # viewing distances
            up, down, left, right = 0, 0, 0, 0
            
            # left
            i = 1
            while c - i >= 0:
                left += 1
                if row[c - i] >= currTree:
                    break
                i += 1
                    
            # right            
            i = 1
            while c + i < len(row):
                right += 1
                if row[c + i] >= currTree:
                    break
                i += 1
                
            # up            
            i = 1
            while r - i >= 0:
                up += 1
                if col[r - i] >= currTree:
                    break
                i += 1            

            # down
            i = 1
            while r + i < len(col):
                down += 1
                if col[r + i] >= currTree:
                    break
                i += 1                        
                    
            score = up * down * left * right
            maxScenicScore = max(maxScenicScore, score)
                
print(maxScenicScore)


