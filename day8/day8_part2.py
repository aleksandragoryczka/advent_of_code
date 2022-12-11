import numpy as np

data = []
with open("input.txt") as f:
    data = f.read().splitlines()

signs_list = []
for line in data:
    signs_list.append([*line]) 
       
arr = np.array(signs_list)

width, length = arr.shape
tree_counter = 0
counters_mmultiplication_list = []
for i in range (1, width-1):
    for j in range(1, length-1):
        current_tree = int(arr[i,j])
        i_counter = 0
        j_counter = 0
        k_counter = 0
        l_counter = 0
        for x in np.flip(arr[:i, j]):
            if current_tree <= int(x):
                j_counter += 1
                break
            else:
                j_counter += 1
        for x in arr[i+1:, j]:
            if current_tree <= int(x):
                k_counter += 1
                break
            else:
                k_counter += 1        
        for x in np.flip(arr[i, :j]):
            if current_tree <= int(x):
                i_counter += 1
                break
            else:
                i_counter += 1

        for x in arr[i, j+1:]:
            if current_tree <= int(x):
                l_counter += 1
                break
            else:
                l_counter += 1
        counters_mmultiplication_list.append(i_counter*j_counter*k_counter*l_counter)


print("The highest scenic score possible for a tree: ", max(counters_mmultiplication_list))