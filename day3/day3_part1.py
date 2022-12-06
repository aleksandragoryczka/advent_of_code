import string

letters_dict = {letter : x for (letter, x) in zip(string.ascii_letters, [x for x in range(1,53)])}

def find_and_prioritize(first_component: list, second_component: list) -> int:
    different_letters = [a for a in set(first_component) if a in set(second_component)]    
    priorities = [letters_dict[l] for l in different_letters]
    return sum(priorities)


ruksacks_list = []

with open("input.txt") as f:
    ruksacks_list = f.read().splitlines()

splited_components_list = []

for rucksack in ruksacks_list:
    splited_components_list.append(rucksack[:len(rucksack)//2] )
    splited_components_list.append(rucksack[len(rucksack)//2:])

shared_compartments = sum([ find_and_prioritize(splited_components_list[i],splited_components_list[i+1]) for i in range(0,len(splited_components_list)-1,2) ])
print("Sum of priorities: ", shared_compartments)