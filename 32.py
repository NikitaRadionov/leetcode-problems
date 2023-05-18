
def anagram(d1, d2, s1, s2):
    if len(d1.keys()) != len(d2.keys()):
        return 0
    if not (s1.issubset(s2) and s2.issubset(s1)):
        return 0

    count = 0
    for k in d1.keys():
        if d1[k] == d2[k]:
            count += 1
    if count == len(d1.keys()):
        return 1
    else:
        return 0


str1 = input()
str2 = input()

s1 = set(str1)
s2 = set(str2)

d1 = {}
d2 = {}


for s in str1:
    d1[s] = d1[s] + 1 if s in d1.keys() else 1

for s in str2:
    d2[s] = d2[s] + 1 if s in d2.keys() else 1

k = anagram(d1, d2, s1, s2)

print(k)
