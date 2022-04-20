def ok(x, y, A):
    return (y + 2*x < A) or (x >= 20) or (y >= 30)
 
l = []
for A in range(80):
    f = True
    for x in range(1000):
        for y in range(1000):
            if not ok(x/10, y/10, A):
               f = False
    if (f): print(A)
