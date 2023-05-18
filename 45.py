
num = 8

num = str(num)

n = len(num)

d = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M"
}

k = 1
rome = []
for i in range(n - 1, -1, -1):
    digit = int(num[i])
    value = digit * k
    if value in d.keys():
        rome.append(d[value])
    else:

        if 1 < value < 4:
            r = ""
            for _ in range(value):
                r += "I"

        if 5 < value < 9:
            r = "V"
            for _ in range(value - 5):
                r += "I"

        if 10 < value < 40:
            r = ""
            for j in range(0, value, 10):
                r += "X"


        if 50 < value < 90:
            r = "L"
            for j in range(0, value - 50, 10):
                r += "X"


        if 100 < value < 400:
            r = ""
            for j in range(0, value, 100):
                r += "C"


        if 500 < value < 900:
            r = "D"
            for j in range(0, value - 500, 100):
                r += "C"


        if 1000 < value:
            r = ""
            for j in range(0, value, 1000):
                r += "M"

        rome.append(r)


    k *= 10

roman = ""

for i in range(len(rome) - 1, -1, -1):
    roman += rome[i]

print(roman)


class Solution:
    def intToRoman(self, num: int) -> str:
        num = str(num)

        n = len(num)

        d = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

        k = 1
        rome = []
        for i in range(n - 1, -1, -1):
            digit = int(num[i])
            value = digit * k
            if value in d.keys():
                rome.append(d[value])
            else:

                if 1 < value < 4:
                    r = ""
                    for _ in range(value):
                        r += "I"

                if 5 < value < 9:
                    r = "V"
                    for _ in range(value - 5):
                        r += "I"

                if 10 < value < 40:
                    r = ""
                    for j in range(0, value, 10):
                        r += "X"


                if 50 < value < 90:
                    r = "L"
                    for j in range(0, value - 50, 10):
                        r += "X"


                if 100 < value < 400:
                    r = ""
                    for j in range(0, value, 100):
                        r += "C"


                if 500 < value < 900:
                    r = "D"
                    for j in range(0, value - 500, 100):
                        r += "C"


                if 1000 < value:
                    r = ""
                    for j in range(0, value, 1000):
                        r += "M"

                rome.append(r)


            k *= 10

        roman = ""

        for i in range(len(rome) - 1, -1, -1):
            roman += rome[i]

        return roman
