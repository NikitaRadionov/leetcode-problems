# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]


# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]
# ]

# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

# matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

# matrix = [[43,39,3,33,37,20,14],[9,18,9,-1,40,22,38],[14,42,3,23,12,14,32],[18,31,45,11,8,-1,31],[28,44,14,23,40,24,13],[29,45,33,45,20,0,45],[12,23,35,32,22,39,8]]

matrix = [[-17, 41, 4, 51, 13],
          [9, 16, 8, -9, -1],
          [25, 21, 0, -10, 18],
          [13, 34, 1, 22, 23],
          [-24, -7, 5, 31, 35]
]




for line in matrix:
    print(line)


def swap(a, b):
    i1, j1 = a
    i2, j2 = b
    c = matrix[i1][j1]
    matrix[i1][j1] = matrix[i2][j2]
    matrix[i2][j2] = c

def is_pos1(pos, p):
    pos1 = [(p, n - 1 - p), (n - 1 - p, n - 1 - p)]
    return pos1[0][0] == pos[0][0] and pos1[0][1] == pos[0][1] and pos1[1][0] == pos[1][0] and pos1[1][1] == pos[1][1]

def is_pos2(pos, p):
    pos2 = [(p, p), (p, n - 1 - p)]
    return pos2[0][0] == pos[0][0] and pos2[0][1] == pos[0][1] and pos2[1][0] == pos[1][0] and pos2[1][1] == pos[1][1]

def is_pos3(pos, p):
    pos3 = [(n - 1 - p, p), (p, p)]
    return pos3[0][0] == pos[0][0] and pos3[0][1] == pos[0][1] and pos3[1][0] == pos[1][0] and pos3[1][1] == pos[1][1]

n = len(matrix)

k = n // 2
count_swap = 3 * k * (n - k)

p = 0
i1, j1 = p, n - 1 - p
i2, j2 = n - 1 - p, n - 1 - p

pos = [(p, n - 1 - p), (n - 1 - p, n - 1 - p)]

s1 = 0

for s in range(1, count_swap + 1):
    swap((i1, j1), (i2, j2))

    if s - s1 == (abs(n - (2 + 2 * p)) + 1):
        s1 = s
        if is_pos1(pos, p):
            pos = [(p, p), (p, n - 1 - p)]
            i1, j1 = (p, p)
            i2, j2 = (p, n - 1 - p)
        elif is_pos2(pos, p):
            pos = [(n - 1 - p, p), (p, p)]
            i1, j1 = (n - 1 - p, p)
            i2, j2 = (p, p)
        elif is_pos3(pos, p):
            p += 1
            pos = [(p, n - 1 - p), (n - 1 - p, n - 1 - p)]
            i1, j1 = (p, n - 1 - p)
            i2, j2 = (n - 1 - p, n - 1 - p)
    else:
        if is_pos1(pos, p):
            j1 -= 1
            i2 -= 1
        elif is_pos2(pos, p):
            i1 += 1
            j2 -= 1
        elif is_pos3(pos, p):
            j1 += 1
            i2 += 1

print()
for line in matrix:
    print(line)
