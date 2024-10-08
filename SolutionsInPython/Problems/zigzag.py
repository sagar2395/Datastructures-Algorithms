def zigzag(s, numRows):
    if numRows == 1:
        return s

    res = ""
    increment = (numRows-1)*2
    strLength = len(s)
    for i in range(numRows):
        for j in range(i, strLength, increment):
            res += s[j]
            resIndex = j + increment - 2*i
            if (i > 0 and i < numRows - 1) and resIndex < strLength:
                res += s[resIndex]
    return res

str = "PAYPALISHIRING"
print(zigzag(str, 4))