# https://codeforces.com/group/pgkaqF4igo/contest/256854/problem/D
# Вася и робот

n = input()
s = input()
x, y = list(map(int, input()))

dx = [0 for i in range(n)]
dy = [0 for i in range(n)]
for i in range(n):
    if s[i] == 'U':
        dy[i] = 1
    if s[i] == 'D':
        dy[i] = -1
    if s[i] == 'L':
        dx[i] = -1
    if s[i] == 'R':
        dx[i] = 1

xx = 0
yy = 0
for i in range(n):
    xx += dx[i]
    yy += dy[i]
