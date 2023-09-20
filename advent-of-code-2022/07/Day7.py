"""
Advent of Code - Day 7

No Space Left On Device

The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). 
The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
cd / switches the current directory to the outermost directory, /.
ls means list. It prints out all of the files and directories immediately contained by the current directory:
123 abc means that the current directory contains a file named abc with size 123.
dir xyz means that the current directory contains a directory named xyz.

    
Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?    
"""
from collections import defaultdict

with open("input.txt") as f:
    commands = [x.strip('\n') for x in f.readlines()]
    
sizes = defaultdict(int)
stack = []

for c in commands:
    if c.startswith("$ ls") or c.startswith("dir"):
        continue
    if c.startswith("$ cd"):
        dest = c.split()[2]
        if dest == "..":
            stack.pop()
        elif dest == "/":
            stack.clear()
            stack.append(dest)
        else:
            path = f"{stack[-1]}_{dest}" if stack else dest
            # value = <value_if_true> if <expression> else <value_if_false>
            stack.append(path)
    else:
        size, file = c.split()
        for path in stack:
            sizes[path] += int(size)
           
       
print(sum(n for n in sizes.values() if n <= 100000))


"""
PART 2

The total disk space available to the filesystem is 70000000. 
To run the update, you need unused space of at least 30000000. 
You need to find a directory you can delete that will free up enough space to run the update.
Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. 
What is the total size of that directory?
"""

to_delete = 30000000 - (70000000 - sizes["/"])
print(min(filter(lambda size: size >= to_delete, sizes.values())))

