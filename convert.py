def convert(s: str, numRows: int) -> str:
    res = ['' for _ in range(numRows)]
    if numRows < 2: return str
    i, flag = 0, -1
    for c in s:
        res[i] += c
        if i == 0 or i == numRows - 1:
            flag = -flag
        i += flag
    return ''.join(res)


a=convert('PAYPALISHIRING',3)
print(a)