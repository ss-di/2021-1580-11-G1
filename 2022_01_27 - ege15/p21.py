def ok(x, y, A):
    return (x>9 or x*x<=A) and (y*y>A or y <=9)
 
l = []
for A in range(256):
    f = True
    for x in range(256):
        for y in range(256):
            if not ok(x, y, A):
               f = False
    if (f): print(A)
