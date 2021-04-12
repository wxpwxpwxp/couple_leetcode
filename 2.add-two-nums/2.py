def twonumbers_sum(m, n):
    a = len(m)
    b = len(n)
    sum1 = sum2 = 0
    for i in range(a):
        #print(m[i])
        sum1 += int(m[i]) * pow(10, i)
    for j in range(b):
        sum2 += (int(n[j]) * pow(10, j))
    sum_final = sum1 + sum2
    c = list(map(int, str(sum_final)))
    d = list(reversed(c))
    return d


if __name__ == '__main__':
    list1 = list(input("1:").split(","))
    list2 = list(input("2:").split(","))
    result = twonumbers_sum(list1,list2)
    print(result)
