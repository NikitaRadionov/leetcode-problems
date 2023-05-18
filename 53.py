a = [38, 54, 105, 207, 325, 504, 171, 940, 720, 942, 450, 680, 505]

x = 0

for i in range(len(a)):
    if a[i] > x:
        x = a[i]

print(x)