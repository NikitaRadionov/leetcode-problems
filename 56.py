n = 4

vmatrix = [[0 for j in range(n)] for i in range(n)]
matrix = [[0 for j in range(n)] for i in range(n)]

# orders:
# "j+", "j-", "i-", "i+"

def order(i, j, now_order):
    if now_order == "j+":
        if j + 1 < n and vmatrix[i][j + 1] == 0:
            j += 1
        elif i + 1 < n and vmatrix[i + 1][j] == 0:
            now_order = "i+"
            i += 1
        elif i - 1 < n and vmatrix[i - 1][j] == 0:
            now_order = "i-"
            i -= 1

        return (i, j, now_order)

    if now_order == "i+":
        if i + 1 < n  and vmatrix[i + 1][j] == 0:
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
        elif i + 1 < n and vmatrix[i + 1][j] == 0:
            now_order = "i+"
            i += 1
        elif i - 1 < n and vmatrix[i - 1][j] == 0:
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

for v in range(1, n * n + 1):
    vmatrix[i][j] = 1
    matrix[i][j] = v
    i, j, now_order = order(i, j, now_order)


for line in matrix:
    print(line)