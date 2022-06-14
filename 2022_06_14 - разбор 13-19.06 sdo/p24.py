with open("107_24.txt") as f:
    s = f.readline()

mcnt = 0
cnt = 0
print(s[:10], len(s))

for i in range(0, len(s), 2):
    if s[i:i+2] in ['AB', 'CB']:
        cnt += 1
        mcnt = max(mcnt, cnt)
    else:
        cnt = 0

cnt = 0
for i in range(1, len(s), 2):
    if s[i:i+2] in ['AB', 'CB']:
        cnt += 1
        mcnt = max(mcnt, cnt)
    else:
        cnt = 0

print(mcnt)
