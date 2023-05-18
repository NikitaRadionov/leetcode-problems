
def gen(n, s="", cl=0, cr=0):
    if cl < n:
        gen(n, s + "(", cl + 1, cr)
    if cr < cl:
        gen(n, s + ")", cl, cr + 1)
    if cl == cr and cl == n:
        print(s)

n = 10
if n > 0:
    gen(n)
else:
    print()