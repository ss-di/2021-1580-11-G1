data = list(map(int, open("27-B.txt").readlines()))
n = data[0]
del data[0]

print(n)

pref = [0] * (n+1)
pref[0] = 0
for i in range(n):
    pref[i+1] = (pref[i] + data[i]) % 999

cnt = 0
for i in range(n):
    print(i)
    for j in range(i+1, n+1):
        if (pref[j] - pref[i]) % 999 == 0:
            cnt += 1
print(cnt)
