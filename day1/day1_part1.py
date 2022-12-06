def slice_sum(i: int, el_nr: int, lista: list) -> int:
    slice = lista[i:el_nr]
    slice_sum = sum([int(var) for var in slice])
    return slice_sum

with open("input.txt") as f:
    elves = f.read().splitlines()

    elves.append("")
    end_line_pos_list = []
    end_line_pos = 0
    while end_line_pos < len(elves):
        end_line_pos = elves.index('', end_line_pos)
        end_line_pos_list.append(end_line_pos)
        end_line_pos += 1

    split_elves_list = []
    i = 0
    for el in end_line_pos_list:
        split_elves_list.append(slice_sum(i, el, elves))
        i = el + 1   

    print("Max: ", max(split_elves_list))
    print("Elf index: ", split_elves_list.index(max(split_elves_list)))

