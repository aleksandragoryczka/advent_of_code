import os
from pathlib import Path

lines_list = []

input_path = "input.txt"

with open(input_path) as f:
    lines_list = f.read().splitlines()

path = os.getcwd()
TREE_PATH = os.path.join(path, "tree_" + input_path.replace(".txt", "\\"))

for line in lines_list:
    cmd_line_split = line.split(" ")
    if cmd_line_split[0] == "$":
        if cmd_line_split[1] == "cd":
            if cmd_line_split[2] == "/":
                if not os.path.isdir(TREE_PATH):
                    os.mkdir(TREE_PATH)
                os.chdir(TREE_PATH)
            elif cmd_line_split[2] == "..":
                os.chdir("..")
            else:
                os.chdir(cmd_line_split[2])
        cwd = os.getcwd()
    elif cmd_line_split[0].isnumeric():
        file_path = os.path.join(cwd, cmd_line_split[0])
        with open(file_path, mode="a"): pass
    elif cmd_line_split[0] == "dir":
        dir_path = os.path.join(cwd, cmd_line_split[1])
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)

# counting
count_dict = {}
def check_path(target_path):
    def count(target_path, folder):
        if target_path in count_dict.keys():
            count_dict[target_path].append(folder)
        else:
            count_dict[target_path] = [folder]

    for file in target_path.iterdir():
        count(target_path.name, file.name)
        if file.is_dir():
            check_path(file)

check_path(Path(TREE_PATH))

def change(k, sum_tmp):
    for val_list in count_dict.values():
        for idx, el in enumerate(val_list):
            if el == k:
                val_list[idx] = sum_tmp
                #count_dict[k] = val_list
                break

def check_var():
    for values_list in count_dict.values():
        res = any(value.isalpha() for value in values_list)
        if res == True:
            return False
    return True

while not check_var():
    print(count_dict)
    for (k, v) in count_dict.items():
        tmp_sum = 0
        if all(value.isnumeric() for value in count_dict[k]):
            tmp_sum = str(sum([int(val) for val in count_dict[k]]))
            change(k, tmp_sum)

print(count_dict)
for (k,v) in count_dict.items():
    v = [int(el) for el in v]
    count_dict[k] = sum(v)
print(count_dict)