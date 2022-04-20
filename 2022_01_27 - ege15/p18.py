def ok(x):
    
    return False or x & int('10000000', 2) == 0 or x & int('111', 2) == 0
 
l = []
for x in range(256):
    if not ok(x):
        print(x)
        l.append(x)

print(len(l))
