def hod(a, mh, h=0):
    if not a > 10:
        if h % 2 == 1:
            return 1
        else:
            return 2
    
    h += 1
    if h > mh:
        return 3
    
    res = []
    res.append(hod(a // 3, mh, h))
    res.append(hod(a - 10, mh, h))
    
    if h % 2 == 1:
        if 1 in res:
            return 1
        elif 3 in res:
            return 3
        else:
            return 2
    else:
        if 2 in res:
            return 2
        elif 3 in res:
            return 3
        else:
            return 1

print(' ', end='\t')
for mh in range(1, 6):
    print(mh, end='\t')
print()

for a in range(11, 200):
    print(a, end='\t')
    for mh in range(1, 6):
        print(hod(a, mh), end='\t')
    print()
