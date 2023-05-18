
matrix = [[1,2,3],[4,5,6],[7,8,9]]

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

v = 0
m = len(matrix) # i
n = len(matrix[0]) # j

vmatrix = [[0 for j in range(n)] for i in range(m)]

# orders:
# "j+", "j-", "i-", "i+"

def order(i, j, now_order):
    if now_order == "j+":
        if j + 1 < n and vmatrix[i][j + 1] == 0:
            j += 1
        elif i + 1 < m and vmatrix[i + 1][j] == 0:
            now_order = "i+"
            i += 1
        elif i - 1 < m and vmatrix[i - 1][j] == 0:
            now_order = "i-"
            i -= 1

        return (i, j, now_order)

    if now_order == "i+":
        if i + 1 < m  and vmatrix[i + 1][j] == 0:
            i += 1
        elif j - 1 > -1 and vmatrix[i][j - 1] == 0:
            now_order = "j-"
            j -= 1
        elif j + 1 < n and vmatrix[i][j + 1] == 0:
            now_order = "j+"
            j += 1

        return (i, j, now_order)

    if now_order == "j-":
        if j - 1 > -1 and vmatrix[i][j - 1] == 0:
            j -= 1
        elif i + 1 < m and vmatrix[i + 1][j] == 0:
            now_order = "i+"
            i += 1
        elif i - 1 < m and vmatrix[i - 1][j] == 0:
            now_order = "i-"
            i -= 1

        return (i, j, now_order)

    if now_order == "i-":
        if i - 1 > - 1 and vmatrix[i - 1][j] == 0:
            i -= 1
        elif j - 1 > -1 and vmatrix[i][j - 1] == 0:
            now_order = "j-"
            j -= 1
        elif j + 1 < n and vmatrix[i][j + 1] == 0:
            now_order = "j+"
            j += 1

        return (i, j, now_order)


i, j = 0, 0
now_order = "j+"
res = []


while v < m * n:
    vmatrix[i][j] = 1
    res.append(matrix[i][j])
    i, j, now_order = order(i, j, now_order)
    v += 1

print(res)