data = list(map(int, open("27-B.txt").readlines()))
n = data[0]
del data[0]

print(n)

prefs = [0] * 999
s = 0
for i in range(n):
    s = (s + data[i]) #% 999
    prefs[s % 999] += 1

cnt = prefs[0] + prefs[0]*(prefs[0]-1) //2

for i in range(1, 999):
    cnt += prefs[i] * (prefs[i]-1) // 2
    
print(cnt)
