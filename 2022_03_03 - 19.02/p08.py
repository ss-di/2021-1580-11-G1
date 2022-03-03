# 466456
import itertools

s = "0123456"

data = list(itertools.product(s, repeat=7))

for i in range(len(data)):
    data[i] = ''.join(data[i])

#print(data)


ans = []
kol = 0
for i in range(len(data)):
    s = data[i]
    if s[0] in ['0', '3', '5']:
        continue
    if '22' in s or '44' in s:
        continue
    ans.append(s)
    kol += 1

#print(ans)    
print(kol)
