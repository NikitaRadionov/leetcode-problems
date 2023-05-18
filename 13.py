# XOR Queries of a Subarray
# https://leetcode.com/problems/xor-queries-of-a-subarray/

arr = [4,8,2,10]
queries = [[2,3],[1,3],[0,0],[0,3]]

n = len(arr)
m = len(queries)

b = [0]

for i in range(n):
    b.append(b[i]^arr[i])

answer = []

for i in range(m):
    l = queries[i][0]
    r = queries[i][1] + 1
    a = b[r]^b[l]
    answer.append(a)

print(answer)
