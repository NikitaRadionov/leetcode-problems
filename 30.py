n = int(input())

prev = None

for i in range(n):
    num = int(input())
    if num != prev or prev is None:
        prev = num
        print(num)