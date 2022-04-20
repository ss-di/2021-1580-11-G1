def hod (a, h, mh, prev=None, pprev=None):
    if a >= 21:
        if h % 2 == 1:
            return 1
        else:
            return 2
    h += 1
    if h > mh:
        return 3
    res = []
    
    if pprev != 1: res.append(hod(a + 1, h, mh, 1, prev))
    if pprev != 2: res.append(hod(a + 2, h, mh, 2, prev))
    if pprev != 3: res.append(hod(a * 2, h, mh, 3, prev))
    
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

print("", end = "\t")
for h in range(1, 7):
    print(h, end="\t")
print()
for a in range(1, 20+1):
    print(a, end = "\t")
    for h in range(1, 7):
        print(hod(a, 0, h), end="\t")
    print()
