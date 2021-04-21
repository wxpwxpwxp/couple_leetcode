def sum_list(nums, target):
    aa = len(nums)
    for i in range(aa):
        for j in range(i+1, aa):
            if nums[i] + nums[j] == target:
                # print(i, j)
                return [i, j]
