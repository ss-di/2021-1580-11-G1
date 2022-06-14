fname = "107_27_0.txt"
fname = "107_27_A.txt" 
fname = "107_27_B.txt"

with open(fname) as f:
    data = f.readlines()

data = list(map(int, data))


n = data[0]
del data[0] # data = data[1:]

best = -1 # 10000000 * 1000 * 3 + 1 # 999999999999999999999999999999999999999999
for z in range(n):
    print(z, n)
    p = 0
    for i in range(z-(n//2), z+n//2):
        p +=  abs(z-i) * data[i % n]

    if best == -1 or p < best:
        best = p
        
print(best * 3)
print(1 * 7 + 0 * 19 + 1 * 8 + 2 * 20 + 3 * 5 + 2 * 13)
