def M(x):
    deviders = []
    kol = 0
    sqrt = round(x**0.5)
    for d in range(2, sqrt + 1):
        if x % d == 0:
            if d != x // d:
                deviders.insert(kol, x // d)
                deviders.insert(kol, d)
            else:
                deviders.insert(kol, d)
                break
            kol += 1
    #print(x, deviders)
    if len(deviders) < 5:
        return 0
    return deviders[-5]
    
kol = 0
for x in range(460000001, 4600000000):
    tmp = M(x)
    if tmp > 0:
        kol += 1
        print(kol, x, tmp)
    if kol == 5:
        break

#M(342)
