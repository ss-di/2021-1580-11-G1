def ok(x):
    p = 37 <= x <= 60
    q = 40 <= x <= 77
    a = False
    return not (p) or (not((q) and not(a)) or not(p))

for x in range(1000):
    x = x/10
    if not ok(x):
        print(x)
