s = open("24.txt").readline()

cnt = [0] * 26 

for c in s:
    cnt[ord(c)-ord("A")] += 1

mx = max(cnt)
mn = min(cnt)

smx = ""
smn = ""

for i in range(26):
    if cnt[i] == mx:
        smx += chr(i + ord("A"))
    if cnt[i] == mn:
        smn += chr(i + ord("A"))

print(smx)
print(smn)

comb = []

for c1 in smx:
    for c2 in smn:
        comb.append(c1+c2)
        comb.append(c2+c1)
        
print(comb)

ans = 0
s = s + ' '
skipnext = False
for i in range(len(s) - 1):
    if skipnext:
        skipnext = False
        continue
    if s[i:i+2] in comb:
        ans += 1
        if s[i+1] in smx:
            skipnext = True
        
print(ans)
