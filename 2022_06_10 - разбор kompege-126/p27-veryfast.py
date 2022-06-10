with open("27-B.txt") as f:
    data = f.readlines()
    
n, maxg = map(int, data[0].split())
del data[0]

data = list(map(int, data))

flag = True
g = 0
full = 0
ans = 0
for x in data:
    if x > 0:
        if x <= maxg - g:
            g += x
        else:
            x -= maxg - g
            full += 1
            g = 0
            full += x // maxg
            g = x % maxg
        ans = max(ans, full + int(g > 0))
    else:
        x = -x
        if g <= x:
            x -= g
            g = 0
            full -= x // maxg
            x = x % maxg
            if x > 0 and full > 0:
                g = maxg-x
                full -= 1
        else:
            g -= x
            
print(ans)
