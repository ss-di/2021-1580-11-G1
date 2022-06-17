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
s = 0
e = 0
su = 0
while (s < n):
    d = e - s
    if su <= k:
        ml = max(ml, e - s)
    if su < k and e < n:
        su += data[e]
        e += 1
    elif su < k:
        break
    else:
        su -= data[s]
        s += 1

print(ml)
