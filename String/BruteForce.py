
'''
******************************************************************************************
 * Text     :  0   1   2   .   .   .   i-j .   .   .   .   i   .   .   n-1
 *             ------------------------|-------------------|------------
 * Pattern  :                          0   .   .   .   .   j   .   .
 *                                     |-------------------|
 ******************************************************************************************
 if fail, new i = i-j+1, j = 0
'''
def bf1(text, pattern):
    i = j = 0
    m, n = pattern.__len__(), text.__len__()
    while j < m and i < n:
        if pattern[j] == text[i]:
            j += 1
            i += 1
        else:
            i -= j-1
            j = 0
    return i - j

def findBf1(text, pattern):
    return bf1(text, pattern) < text.__len__()-pattern.__len__()
'''
******************************************************************************************
 * Text     :  0   1   2   .   .   .   i   i+1 .   .   .   i+j .   .   n-1
 *             ------------------------|-------------------|------------
 * Pattern  :                          0   1   .   .   .   j   .   .
 *                                     |-------------------|
 ******************************************************************************************
'''
def bf2(text, pattern):
    i = j = 0
    m, n = pattern.__len__(), text.__len__()
    for i in range(0, n-m+1):
        j = 0
        while j < m:
            if not text[i+j] == pattern[j]:
                break
            j += 1
        if j >= m:
            break
    return i

def findBf2(text, pattern):
    return bf1(text, pattern) < text.__len__()-pattern.__len__()+1

if __name__ == '__main__':
    t = "this is a string match test0"
    p = "0"
    print "length of t: %s" % t.__len__()
    print bf1(t, p)
    print"length of n-m: %s" % str(t.__len__()-p.__len__()+1)
    print bf2(t, p)
