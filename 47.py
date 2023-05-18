salary = [4000, 3000, 1000, 2000]
mx = 0
mn = None
summ = 0
n = len(salary)
for i in range(n):
    summ += salary[i]
    if mn is None or mn > salary[i]:
        mn = salary[i]
    if salary[i] > mx:
        mx = salary[i]
average = (summ - mn - mx) / (n - 2)
print(average)