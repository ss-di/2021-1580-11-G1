with open("27-B.txt") as f:
    data = f.readlines()
    
n, maxg = map(int, data[0].split())
del data[0]

data = list(map(int, data))

flag = True
g = []
cnt = 0
for x in data:
    cnt = cnt + 1
    if cnt % 1000 == 0:
        print(cnt)
    if x > 0:
        i = 0
        while x > 0:
            if i >= len(g):
                g.append(0)
            if g[i] < maxg:
                if maxg - g[i] >= x:
                    g[i] += x
                    x = 0
                else:
                    x -= maxg - g[i]
                    g[i] = maxg
                    i += 1
            else:
                i += 1
    else:
        i = 0
        x = -x
        while x > 0 and i < len(g):
            if g[i] <= x:
                x -= g[i]
                g[i] = 0
                i += 1
            else:
                g[i] -= x
                x = 0
            
                
print(len(g))
