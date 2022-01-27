def d(x, y):
    return x % y == 0
    
def ok(x):
    a = 1000000000 #12
    return d(x, a) or (not d(x, 6) or not d(x, 4))

for x in range(150):
    if not ok(x):
        print(x)
