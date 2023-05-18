n = 7

a = n

while a != 1 and a > 9:
    s = str(a)
    a = 0
    for i in range(len(s)):
        a += int(s[i]) ** 2

if a == 1 or a == 7:
    print(True)
else:
    print(False)
