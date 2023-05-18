n = int(input())

mx = 0
count = 0
for i in range(n):
    num = int(input())
    if num == 1:
        count += 1
        if count > mx:
            mx = count
    else:
        count = 0

print(mx)
