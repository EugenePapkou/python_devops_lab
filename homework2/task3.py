file_input = open("input.txt", "r")
strings = file_input.readlines()

# retrieving w and h from file
temp_list = strings[0].split()
w = int(temp_list[0])
h = int(temp_list[1])

# retrieving n from file
temp_list = strings[1].split()
n = int(temp_list[0])

# coordinates of every rectangle
coord = {}

for j, i in enumerate(range(2, n + 2)):
    temp_list = strings[i].split()
    coord[j] = temp_list

# entering '0' in matrix which has size the same as w * h
matrix = [[0 for i in range(w)] for n in range(h)]
print(matrix)
# entering '1' on the area where rectangles were painted
for i in range(n):
    x1 = int(coord[i][0])
    x2 = int(coord[i][2])
    y1 = int(coord[i][1])
    y2 = int(coord[i][3])
    for n in range(x1, x2):
        for k in range(y1, y2):
            matrix[n][k] = 1

# counting '1' in matrix
s = 0
for i in range(h):
    s += sum(matrix[i])

# free area
square = w * h - s
if w >= 1 and h <= 100 and 0 <= n <= 5000:
    print("Free area is: ", square)
