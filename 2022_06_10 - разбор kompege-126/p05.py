def avt(n):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        return '11' + n2 + '0'
    else:
        return '1' + n2 + '00'

d = {}
for i in range(1, 256):
    res = avt(i)
    d[res] = d.get(res, 0) + 1

cnt = 0
for k in d.keys():
    if d[k] > 1:
        print(k, d[k])
        cnt += 1

print(cnt)
