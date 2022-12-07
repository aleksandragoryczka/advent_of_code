string = ""

with open("input.txt") as f:
    string= f.read()

string_list = list(string)

for i in range(len(string_list)):
    tmp_slice = string_list[i:i+4]
    if len(set(tmp_slice)) == 4:
        marker = i+4
        break

print("Characters to be processed before the first start-of-packet marker is detected:", marker)