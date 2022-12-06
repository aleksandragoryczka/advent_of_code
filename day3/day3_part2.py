import string

letters_dict = {letter : x for (letter, x) in zip(string.ascii_letters, [x for x in range(1,53)])}

def find_and_prioritize(first_component: list, second_component: list, third_component: list) -> int:
    different_letters = [a for a in set(first_component) if a in set(second_component) and a in set(third_component)]
    priorities_sum = sum([letters_dict[priority] for priority in different_letters])
    return priorities_sum

rucksacks_list = []

with open("input.txt") as f:
    rucksacks_list = f.read().splitlines()


shared_compartments = sum([ find_and_prioritize(rucksacks_list[i], rucksacks_list[i+1],rucksacks_list[i+2]) for i in range(0,len(rucksacks_list)-2,3) ])
print("Sum of priorities: ", shared_compartments)