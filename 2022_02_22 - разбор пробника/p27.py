data = list(map(int, open("27_B.txt").readlines()))
n = data[0]
del data[0]
d = 67

#print(data)


sums = [None] * (n+1)
mins = [None] * 67
maxs = [None] * 67

sums[0] = 0

mins[0] = 0
maxs[0] = 0

for i in range(n):
    sums[i+1] = sums[i] + data[i]
    ost = sums[i+1] % d
    if mins[ost] is None:
        mins[ost] = i + 1
        maxs[ost] = i + 1
    else:
        maxs[ost] = i + 1
        
# b e ms
ms = -1
for i in range(d):
    if mins[i] is not None:
        cs = sums[maxs[i]] - sums[mins[i]]
        cl = maxs[i] - mins[i]
        if cs > ms:
            ms = cs
            ml = cl
        elif cs == ms:
            if cl < ml:
                ml = cl
        
print(ms, ml)
