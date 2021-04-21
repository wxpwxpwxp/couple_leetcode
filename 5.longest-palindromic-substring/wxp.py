def re_str(s):
    tmp = []
    result = []
    tag = []
    for i in range(len(s)):
        if s[i] not in tmp:
            tmp.append(s[i])
        else:
            pos = tmp.index(s[i])
            tag.append(s[i])
            result.append(len(tmp) - pos + 1)
            tmp.append(s[i])
    if len(result) == 0:
        return s[0]
    p = 0
    p = max(result)
    k = result.index(p)
    j = q = n =0
    a = []
    for j in range(len(s)):
        if tag[k] == s[j]:
            q = j
            break
    while n < p:
        a.append(s[q])
        q += 1
        n += 1
    return a
