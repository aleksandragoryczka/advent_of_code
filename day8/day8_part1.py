import numpy as np

data = []
with open("input.txt") as f:
    data = f.read().splitlines()

signs_list = []
for line in data:
    signs_list.append([*line]) 
       
arr = np.array(signs_list)

width, length = arr.shape
edge_trees = 2* width + 2*length - 4
tree_counter = 0
for i in range (1, width-1):
    for j in range(1, length-1):
        current_tree = int(arr[i,j])
        j_flag = True
        i_flag = True
        k_flag = True
        l_flag = True

        for x in arr[:i, j]:
            if current_tree <= int(x):
                j_flag = False
                break
        for x in arr[i+1:, j]:
            if current_tree <= int(x):
                k_flag = False
                break
        for y in arr[i, :j]:
            if current_tree <= int(y):
                i_flag = False
                break
        for y in arr[i, j+1:]:
            if current_tree <= int(y):
                l_flag = False
                break
        if any([j_flag, i_flag, k_flag, l_flag]):
            tree_counter += 1


vis_trees = tree_counter + edge_trees
print("Trees visible from outside the grid: ", vis_trees)