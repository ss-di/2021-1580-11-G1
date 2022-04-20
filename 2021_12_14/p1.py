#  (!z)x+xy

def f(x, y, z):
    return (not (x or y)) or (y==z)

for x in False, True:
    for y in False, True:
        for z in False, True:
            if not f(x, y, z):
                print(int(z), int(x), int(y), int(f(x, y, z)))
