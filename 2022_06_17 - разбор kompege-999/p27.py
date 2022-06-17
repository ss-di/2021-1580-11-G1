fname = '270.txt'
fname = '27A.txt'
fname = '27B.txt'

with open(fname) as f:
    data = f.readlines()

n, k = map(int, data[0].split())
del data[0]
data = data[:n]
data = list(map(int, data))
#print(n, k, data)

#n, k = 5, 10
#data = [1, 1, 1, 1, 1]

ml = 0
for s in range(n):
    print(s, n, s/n*100)
    for e in range(s+1, n+1):
        su = sum(data[s:e])
        d = e-s
        if su <= k:
            ml = max(ml,d)
        else:
            break
print(ml)
