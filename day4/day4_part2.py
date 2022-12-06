def check_is_overlapping(section_one_range: str, section_two_range: str) -> int:
    first = set([i for i in range (int(section_one_range.split("-")[0]), int(section_one_range.split("-")[1])+1)])
    second = set([i for i in range (int(section_two_range.split("-")[0]), int(section_two_range.split("-")[1])+1)])


    var = [True if val in second else False for val in first]

    if True in var:
        return 1
    return 0



sections_list = []

with open("input.txt") as f:
        sections_list = f.read().replace(",", "\n")

sections_list = sections_list.splitlines()


overlapped_sections = sum([ check_is_overlapping(sections_list[i],sections_list[i+1]) for i in range(0,len(sections_list)-1,2) ])
print("Number of pairs with overlappping sections: ", overlapped_sections)