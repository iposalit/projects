"""
Advent of Code - Day 1

Elves calories list

"""

file1 = open('input.txt', 'r')
calories = [entry.strip() for entry in file1.readlines()]

elves_calories = []
calories_sum = 0

for entry in calories:
    if entry != '':
        calories_sum += int(entry)
    else:
        elves_calories.append(calories_sum)
        calories_sum = 0 # reset to 0 before next elf's items

print(max(elves_calories))

# PART 2
sorted_list = sorted(elves_calories, reverse=True)
print(sum(sorted_list[0:3]))
