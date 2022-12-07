import re

input = []

with open("input.txt") as f:
    input = f.read().split("\n\n")

starting_stacks = input[0].split("\n")
stacks_numbers = sum([el.strip().isalnum() for el in starting_stacks[-1]])
starting_stacks = list(reversed(starting_stacks[:-1]))


narrowing_stacks = []

for row in starting_stacks:
    x = row.replace(" [", "[")
    y = x.replace("] ", "]")
    z = y.replace("   ", ".")
    narrowing_stacks.append(z)

stacks = []
for i in range(stacks_numbers):
    stacks.append([])


for id, row in enumerate(narrowing_stacks):
    tmp = 0

    m = re.search(r'\.\.\.\.\s', row)
    if m:
        row = row.replace(".", "", 1)
    for idx, sign in enumerate(row):        
        if sign == ".":
            len = 0
            tmp += 1
        if sign == "[":
            stacks[tmp].append(row[idx+1])
            tmp += 1


rules = input[1].splitlines()
for row in rules:
    numbers_list = re.findall(r'\d+', row)

    for i in range(int(numbers_list[0])):
        stacks[int(numbers_list[2])-1].append(stacks[int(numbers_list[1])-1][-1])
        stacks[int(numbers_list[1])-1].pop()  

stacks_top_string = "".join([stack[-1] for stack in stacks])
print("Message on top of stacks: ", stacks_top_string)
    


