
#fname = "107_27_0.txt"
fname = "107_27_A.txt"
fname = "107_27_B.txt"

with open(fname) as f:
    data = f.readlines()

data = list(map(int, data))

#print(data)

n = data[0]
del data[0] # data = data[1:]

data = data + data + data

sums = [0]
for z in range(3*n):
    sums.append(sums[-1] + data[z])

best = -1 # 10000000 * 1000 * 3 + 1 # 999999999999999999999999999999999999999999

#print(data)
#print(sums)

z=n
p = 0
for i in range(z+-n//2, z+n//2):
    p +=  abs(z - i) * data[i]
best = p
#print(p)

for z in range(z+1, z+n):
    if z % 1000 == 0:
        print(z, n, int(z/n*100))
    #print (sums[z] - sums[z-n//2], sums[z+n//2] - sums[z])
    p = p + ( sums[z] - sums[z-n//2] ) - ( sums[z+n//2] - sums[z] )
    #print(p)
    if best == -1 or p < best:
        best = p
        
print(best*3)


'''
102
98
120
114
118
96

96
'''
