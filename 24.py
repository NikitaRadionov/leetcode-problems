nums = [1, 2, 3]
res = set()

def recursion(res, nums, data = []):
    if len(nums) > 1:
        for i in range(len(nums)):
            res.add(tuple(data + nums))
            data.append(nums[0])
            recursion(res, nums[1:], data)
            data.pop()
            nums = nums[1:] + [nums[0]]

recursion(res, nums)
print(list(map(list, list(res))))
