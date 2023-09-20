"""
Advent of Code - Day 6

Tuning Trouble

the start of a packet is indicated by a sequence of four characters that are all different

Example:
bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5

How many characters need to be processed before the first start-of-packet marker is detected?
"""
with open("input.txt") as f:
    line = f.readline()

# n = the number of distinct characters that represent a marker
def findMarker(n):    
    for i in range(len(line) - n):        
        if len(set(line[i:i+n])) == n:
            return i + n
            
print(findMarker(4))

"""
PART 2
A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.
How many characters need to be processed before the first start-of-message marker is detected?
"""            

print(findMarker(14))



