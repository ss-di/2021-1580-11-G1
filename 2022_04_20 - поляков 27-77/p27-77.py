import math

#o5 = [[] for i in range(5)]
#o7 = [[] for i in range(7)]

o5 = [None] * 5
o7 = [None] * 7

s = 0
with open("27-77b.txt") as f:
    n = int(f.readline())
    for i in range(n):
        d = list(map(int, f.readline().split()))
        lcm = set()
        m = len(d)
        for j in range(1, m - 1):
            for k in range(j + 1, m):
                lcm.add(d[j] // math.gcd(d[j],d[k]) * d[k])
        mx = max(lcm)
        s += mx
        for a in lcm:
            if a != mx:
                co5 = o5
                ost5 = a%5
                razn5 = mx - a
                for o in range(5):
                    if not (o5[o] is None):
                        newost5 = (o + ost5) % 5
                        if co5[newost5] is None:
                            co5[newost5] = o5[o] + razn5
                        else:
                            co5[newost5] = min(co5[newost5], o5[o] + razn5)
                if co5[ost5] is None:
                    co5[ost5] = razn5
                else:
                    co5[ost5] = min(co5[ost5], razn5)
                o5 = co5
            
                co7 = o7
                ost7 = a%7
                razn7 = mx - a
                for o in range(7):
                    if not (o7[o] is None):
                        newost7 = (o + ost7) % 7
                        if co7[newost7] is None:
                            co7[newost7] = o7[o] + razn7
                        else:
                            co7[newost7] = min(co7[newost7], o7[o] + razn7)
                if co7[ost7] is None:
                    co7[ost7] = razn7
                else:
                    co7[ost7] = min(co7[ost7], razn7)
                o7 = co7
            
if s % 5 == 0 and s % 7 == 0:
    if o5[0] is None:
        if o7[0] is None:
            print('err')
        else:
            print(s - o7[0])
    else:
        if o7[0] is None:
            print(s - o5[0])
        else:
            print(s - min(o7[0], o5[0]))
elif s % 5 == 0 or s % 7 == 0:
    print(s)
else:
    a = o5[s % 5]
    b = o7[s % 7]
    if a is None:
        if b is None:
            print('err')
        else:
            print(s - b)
    else:
        if b is None:
            print(s - a)
        else:
            print(s - min(a, b))
