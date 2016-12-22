
def match(text, pattern):
    next = buildNext(pattern)
    i = j = 0
    m, n = pattern.__len__(), text.__len__()
    while j<m and i<n:
        if j<0 or text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    return i - j

def buildNext(pattern):
    next = [-1]
    j, t = 0, -1
    m = pattern.__len__()
    while j < m-1:
        if t<0 or pattern[j] == pattern[t]:
            t += 1
            j += 1
            next.append(t)
        else:
            t = next[t]
    print next
    return next

if __name__ == '__main__':
    ts = "1010011100010"
    p = "11100"
    a = "*11100"
    #p = "00001"

    print"length of n-m: %s" % str(ts.__len__()-p.__len__())
    print match(ts, p)
