def ok(x):
    m1 = [2, 4, 6, 8, 10, 12]
    m2 = [4, 8, 12, 116]
    a = []
    return x not in m1 or (not(x in m2 and not x in a) or not(x in m1))

for x in range(150):
    if not ok(x):
        print(x)
