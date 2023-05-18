def fib(n, m):
    dp2_start = 0
    dp1_start = 1

    dp_2 = 1 % m
    dp_1 = 2 % m

    table = [0 % m, 1 % m, 1 % m]
    pi = 2
    while not (dp_2 == dp2_start and dp_1 == dp1_start):
        pi += 1
        table.append(dp_1)
        dp = (dp_1 + dp_2) % m
        dp_2 = dp_1
        dp_1 = dp

    return table[n % pi]


def main():
    n, m = map(int, input().split())
    print(fib(n, m))


if __name__ == "__main__":
    main()