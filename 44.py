s = "PAYPALISHIRING"
nR = 3
# s = "A"
# nR = 7


b = 2*nR - 2

if b > 0:
    n = len(s)

    lines = ["" for _ in range(nR)]

    modes = [(0, 0) for _ in range(nR)]

    for i in range(nR):
        modes[i] = (i, b - i)


    for k in range((n // b) + 1):
        for i in range(nR):
            if 0 < i < nR - 1:
                if b*k + modes[i][0] < n:
                    lines[i] += s[b*k + modes[i][0]]
                if b*k + modes[i][1] < n:
                    lines[i] += s[b*k + modes[i][1]]
            else:
                if b*k + modes[i][0] < n:
                    lines[i] += s[b*k + modes[i][0]]
    res = ""
    for i in range(nR):
        res += lines[i]

    print(res)
else:
    print(s)


class Solution:
    def convert(self, s: str, nR: int) -> str:
        b = 2*nR - 2

        if b > 0:
            n = len(s)

            lines = ["" for _ in range(nR)]

            modes = [(0, 0) for _ in range(nR)]

            for i in range(nR):
                modes[i] = (i, b - i)


            for k in range((n // b) + 1):
                for i in range(nR):
                    if 0 < i < nR - 1:
                        if b*k + modes[i][0] < n:
                            lines[i] += s[b*k + modes[i][0]]
                        if b*k + modes[i][1] < n:
                            lines[i] += s[b*k + modes[i][1]]
                    else:
                        if b*k + modes[i][0] < n:
                            lines[i] += s[b*k + modes[i][0]]
            res = ""
            for i in range(nR):
                res += lines[i]

            return res
        else:
            return s