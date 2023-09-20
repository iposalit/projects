"""
Advent of Code - Day 2

Rock Paper Scissors

0 - loss
3 - tie
6 - win

Score for shape used:
1 - Rock
2 - Paper
3 - Scissors

Total Score is sum across all rounds

First column:
A = Rock
B = Paper
C = Scissors

Second column (your move):
X = Rock
Y = Paper
Z = Scissors

Rock > Scissors
Scissors > Paper
Paper > Rock

# win
C X
A Y
B Z

# tie
A X
B Y
C Z

PART 2 Revision
second column is actually how the round should end
X = 0
Y = 3
Z = 6

"""

import pandas as pd

df = pd.read_csv('input.txt', sep=' ', header=None, names=["Opponent", "Me"])

# PART 1
shape_score = {'X':1, 'Y':2, 'Z':3}
win = [('C', 'X'), ('A', 'Y'), ('B', 'Z')]
tie = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]

score = 0
zipped = list(zip(df['Opponent'], df['Me']))
for i in zipped:
    score += shape_score[i[1]]
    if i in win:
        score += 6        
    elif i in tie:
        score += 3
    else:
        continue
print(score)

# PART 2
win_score = {'X':0, 'Y':3, 'Z':6}
shape_score = {'A':1, 'B':2, 'C':3}
win = {'A':'B', 'B':'C', 'C':'A'}
lose = {'A':'C', 'B':'A', 'C':'B'}

new_score = 0
for i in zipped:
    new_score += win_score[i[1]]    
    if i[1] == 'X': # lose
        new_score += shape_score[lose[i[0]]]
    elif i[1] == 'Z': # win
        new_score += shape_score[win[i[0]]]
    else: # draw
        new_score += shape_score[i[0]]
print(new_score)

