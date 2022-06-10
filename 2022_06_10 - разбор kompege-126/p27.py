with open("27-B.txt") as f:
    data = f.readlines()
    
n, maxg = map(int, data[0].split())
del data[0]

data = list(map(int, data))

flag = True
cnt = -1
while flag:
    cnt += 1
    flag = False
    g = 0
    for i in range(len(data)):
        if data[i] > 0:
            flag = True
            if maxg - g >= data[i]:
                g += data[i]
                data[i] = 0
            else:
                data[i] -= maxg - g
                g = maxg
        else:
            if g <= -data[i]:
                data[i] += g
                g = 0
            else:
                g = g + data[i]
                data[i] = 0
    print(cnt)
            
                
print(cnt)
