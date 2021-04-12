def repeat_str(s):
    if len(s) == 0:
        return 0
    tmp = []
    result = []
    for i in range(len(s)):
        if s[i] not in tmp:
            tmp.append(s[i])
        else:
            result.append(len(tmp))
            pos = tmp.index(s[i])
            tmp = tmp[(pos + 1):]
            tmp.append(s[i])
    result.sort()
    return result[len(result) - 1]


if __name__ == '__main__':
    s = list(input("str:"))
    n = repeat_str(s)
    print(n)
