def f(w, x, y, z):
    return (w or y) and (not x or not z) and not w
    
zn = [False, True]
for w in zn:
    for x in zn:
        for y in zn:
            for z in zn:
                if f(w, x, y, z):
                    print (int(y), int(x), int(w), int(z), int(f(w, x, y, z)))
