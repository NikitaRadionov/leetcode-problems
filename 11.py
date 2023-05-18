nums = [10, 4, 8, 3]
n = len(nums)
leftSum = [None for i in range(n)]
rightSum = [None for i in range(n)]

lsum = 0
rsum = 0
for i in range(n):
    leftSum[i] = lsum
    rightSum[n - (i + 1)] = rsum
    lsum += nums[i]
    rsum += nums[n - (i + 1)]

answer = [abs(leftSum[i] - rightSum[i]) for i in range(n)]

print(answer)
