def sum_list(nums, target):
    aa = len(nums)
    for i in range(aa):
        for j in range(i+1, aa):
            if nums[i] + nums[j] == target:
                # print(i, j)
                return [i, j]


if __name__ == '__main__':
    n = list(map(int, input("please input some numbers:").split(",")))
    t = int(input("please input a number:"))
    b = sum_list(n, t)
    print(b)
